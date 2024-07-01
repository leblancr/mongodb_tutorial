from decimal import Decimal
from bson.decimal128 import Decimal128
from bson.codec_options import TypeCodec, TypeRegistry, CodecOptions
import pprint


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
    
    
def run(client):
    print(f"Running {__name__}.py")
 
    try:
        client.drop_database("custom_type_example")
        db = client.custom_type_example
        num = Decimal("45.321")
        decimal_codec = DecimalCodec()
        type_registry = TypeRegistry([decimal_codec])
        codec_options = CodecOptions(type_registry=type_registry)
        collection = db.get_collection("test", codec_options=codec_options)
        collection.insert_one({"num": num})
        mydoc = collection.find_one()
        pprint.pprint(mydoc)
    except Exception as e:
        print(f"An error occurred: {e}")
        
             