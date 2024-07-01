from decimal import Decimal
from bson.decimal128 import Decimal128
from bson.codec_options import TypeCodec, TypeRegistry, CodecOptions, TypeDecoder
from bson.binary import Binary
from bson.binary import Binary, USER_DEFINED_SUBTYPE

import pprint
import pickle


# The type codec
class DecimalCodec(TypeCodec):
    python_type = Decimal  # the Python type acted upon by this type codec
    bson_type = Decimal128  # the BSON type acted upon by this type codec

    def transform_python(self, value):
        """Function that transforms a custom type value into a type
        that BSON can encode."""
        return Decimal128(value)

    def transform_bson(self, value):
        """Function that transforms a vanilla BSON type value into our
        custom type."""
        return value.to_decimal()
    
    
# custom types
class MyStringType(object):
    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return "MyStringType('%s')" % (self.__value,)


class MyNumberType(object):
    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return "MyNumberType(%s)" % (self.__value,)


def fallback_pickle_encoder(value):
    return Binary(pickle.dumps(value), USER_DEFINED_SUBTYPE)


class PickledBinaryDecoder(TypeDecoder):
    bson_type = Binary

    def transform_bson(self, value):
        if value.subtype == USER_DEFINED_SUBTYPE:
            return pickle.loads(value)
        return value


def fallback_encoder(value):
    if isinstance(value, Decimal):
        return Decimal128(value)

    return value


def run(client):
    # use the codec
    print(f"Running {__name__}.py")
 
    try:
        client.drop_database("custom_type_example")
        db = client.custom_type_example  # create new database

        num = Decimal("45.321")  # python Deciml object

        decimal_codec = DecimalCodec()  # instance of our type codec class above
        type_registry = TypeRegistry([decimal_codec])  # register the codec with PyMongo
        codec_options = CodecOptions(type_registry=type_registry)  # CodecOptions instance with our type_registry

        # get a Collection object that understands the Decimal data type
        # test gets created when a document gets inserted
        collection = db.get_collection("test", codec_options=codec_options)
        collection.insert_one({"num": num})  # encode instance of Decimal

        mydoc = collection.find_one()  # decode instance of Decimal128
        pprint.pprint(mydoc)

        vanilla_collection = db.get_collection("test")
        pprint.pprint(vanilla_collection.find_one())

        # binary
        newcoll = db.get_collection("new")
        newcoll.insert_one({"_id": 1, "data": Binary(b"123", subtype=0)})
        doc = newcoll.find_one()
        print(type(doc["data"]))

        # fallback_encoder
        type_registry = TypeRegistry(fallback_encoder=fallback_encoder)
        codec_options = CodecOptions(type_registry=type_registry)
        collection = db.get_collection("test", codec_options=codec_options)
        collection.drop()  # why?

        collection.insert_one({"num": Decimal("45.321")})
        mydoc = collection.find_one()
        pprint.pprint(mydoc)

        # Encoding unknown types
        codec_options = CodecOptions(
            type_registry=TypeRegistry(
                [PickledBinaryDecoder()], fallback_encoder=fallback_pickle_encoder
            )
        )

        collection = db.get_collection("test_fe", codec_options=codec_options)
        collection.insert_one(
            {"_id": 1, "str": MyStringType("hello world"), "num": MyNumberType(2)}
        )

        mydoc = collection.find_one()
        assert isinstance(mydoc["str"], MyStringType)
        assert isinstance(mydoc["num"], MyNumberType)
        pprint.pprint(mydoc)
    except Exception as e:
        print(f"An error occurred: {e}")
        
             