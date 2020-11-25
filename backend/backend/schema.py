from graphene import ObjectType,Schema
import graphql_jwt

class Query(
    ObjectType
    ):
    pass


class Mutation(
    ObjectType
    ):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema=Schema(mutation=Mutation)