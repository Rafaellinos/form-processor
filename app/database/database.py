from typing import List

import aioboto3
import logging
from boto3.dynamodb.conditions import Key
from uuid import uuid4, UUID
from datetime import datetime

from app.config.settings import get_settings
from app.models.schemas.simple_form import SimpleForm


class Database:

    @staticmethod
    async def connect():
        logging.info("Connecting to database")

    @staticmethod
    async def get_session():
        return aioboto3.Session()

    @staticmethod
    async def get_items() -> List[SimpleForm]:
        session = await Database.get_session()
        async with session.resource('dynamodb', region_name=get_settings().AWS_DEFAULT_REGION) as dynamodb:
            table = await dynamodb.Table(get_settings().DYNAMODB_TABLE_NAME)
            result = await table.scan()
            logging.debug("boto return: %s", result)
            items: list = result.get("Items", [])
            if not items:
                return []
            return [SimpleForm(**item) for item in items]

    @staticmethod
    async def get_item_by_id(item_id: UUID) -> SimpleForm | None:
        session = await Database.get_session()
        async with session.resource('dynamodb', region_name=get_settings().AWS_DEFAULT_REGION) as dynamodb:
            table = await dynamodb.Table(get_settings().DYNAMODB_TABLE_NAME)
            result = await table.query(
                KeyConditionExpression=Key('id').eq(str(item_id))
            )
            logging.debug("boto return: %s", result)
            items: list = result.get("Items", [])
            if not items:
                return None
            return SimpleForm(**items[0])

    @staticmethod
    async def put_item(simple_form_data: SimpleForm) -> SimpleForm:
        session = await Database.get_session()
        async with session.resource('dynamodb', region_name=get_settings().AWS_DEFAULT_REGION) as dynamodb:
            table = await dynamodb.Table(get_settings().DYNAMODB_TABLE_NAME)
            result = await table.put_item(
                Item={
                    "id": str(uuid4()),
                    "date": datetime.today().isoformat(),
                    **simple_form_data.dict(),
                }
            )
            logging.debug("boto return: %s", result)
            return result
