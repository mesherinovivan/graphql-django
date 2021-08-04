import graphene
from graphene_django.debug import DjangoDebug
from contact.schema import schema as contact_schema


class Query(
        contact_schema.Query,
        graphene.ObjectType,
    ):
        debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    contact_schema.Mutation,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
