# from django_elasticsearch_dsl import (
#     Document , fields , Index
# )
# from .models import Item
# from django_elasticsearch_dsl.registries import registry
#
# PUBLISHER_INDEX = Index('elastic_demo')
#
# PUBLISHER_INDEX.settings(
#     number_of_shards = 1,
#     number_of_replicas = 1
# )
# @PUBLISHER_INDEX.doc_type
# @PUBLISHER_INDEX.document
# @registry.register_document
#
# class NewsDocument(Document):
#     id = fields.IntegerField(attr="id")
#     word = fields.TextField(
#          fields = {
#              "raw" : {
#                  "type" : 'keyword'
#              }
#          }
#      )
#
#     wordTrans = fields.TextField(
#          fields = {
#              "raw" : {
#                  "type" : 'keyword'
#              }
#          }
#      )
#
# class Django(object):
#     model = Item