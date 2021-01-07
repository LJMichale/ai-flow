#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import time
import uuid

from mongoengine import connect
from notification_service.event_storage import BaseEventStorage
from notification_service.base_notification import BaseEvent
from notification_service.mongo_notification import MongoEvent


class MongoEventStorage(BaseEventStorage):
    def __init__(self, *args, **kwargs):
        self.db_conn = self.setup_connection(**kwargs)
        self.server_id = str(uuid.uuid4())

    def setup_connection(self, **kwargs):
        db_conf = {
            "host": kwargs.get("host"),
            "port": kwargs.get("port"),
            "username": kwargs.get("username"),
            "password": kwargs.get("password"),
            "db": kwargs.get("db"),
        }
        # If ignore the authSource, the authentication will be failed.
        conn_uri = "mongodb://{username}:{password}@{host}:{port}/{db}?authSource=admin".format(**db_conf)
        db_conf["host"] = conn_uri
        return connect(
            connect=False,
            **db_conf)

    def get_latest_version(self, key: str = None):
        mongo_events = MongoEvent.get_by_key(self.server_id, key, 0, 1, "-version")
        if not mongo_events:
            return 0
        return mongo_events[0].version

    def add_event(self, event: BaseEvent):
        kwargs = {
            "server_id": self.server_id,
            "create_time": time.time_ns(),
            "event_type": event.event_type,
            "key": event.key,
            "value": event.value,
        }
        mongo_event = MongoEvent(**kwargs)
        mongo_event.save()
        mongo_event.reload()
        event.create_time = mongo_event.create_time
        event.version = mongo_event.version
        event.id = mongo_event.auto_increase_id
        return event

    def list_events(self, key: str, version: int = None):
        res = MongoEvent.get_base_events_by_version(self.server_id, key, version)
        return res

    def list_all_events(self, start_time: int):
        res = MongoEvent.get_base_events_by_time(self.server_id, start_time)
        return res

    def list_all_events_from_id(self, id: int):
        res = MongoEvent.get_base_events_by_id(self.server_id, id)
        return res

    def clean_up(self):
        MongoEvent.delete_by_client(self.server_id)