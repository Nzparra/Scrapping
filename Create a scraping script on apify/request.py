import http.client

conn = http.client.HTTPSConnection("api.opensea.io")

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.io)",
 "Content-Type": "application/json" 
}

payload = "{\"id\":\"rankingsQuery\",\"query\":\"query rankingsQuery(\\n  $chain: [ChainScalar!]\\n  $count: Int!\\n  $cursor: String\\n  $sortBy: CollectionSort\\n  $parents: [CollectionSlug!]\\n  $createdAfter: DateTime\\n) {\\n  ...rankings_collections\\n}\\n\\nfragment rankings_collections on Query {\\n  collections(after: $cursor, chains: $chain, first: $count, sortBy: $sortBy, parents: $parents, createdAfter: $createdAfter, sortAscending: false, includeHidden: true, excludeZeroVolume: true) {\\n    edges {\\n      node {\\n        createdDate\\n        name\\n        slug\\n        logo\\n        stats {\\n          floorPrice\\n          marketCap\\n          numOwners\\n          totalSupply\\n          sevenDayChange\\n          sevenDayVolume\\n          oneDayChange\\n          oneDayVolume\\n          thirtyDayChange\\n          thirtyDayVolume\\n          totalVolume\\n          id\\n        }\\n        id\\n        __typename\\n      }\\n      cursor\\n    }\\n    pageInfo {\\n      endCursor\\n      hasNextPage\\n    }\\n  }\\n}\\n\",\"variables\":{\"count\":100,\"cursor\":\"\",\"sortBy\":\"SEVEN_DAY_VOLUME\"}}"

conn.request("GET", "/graphql/", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))