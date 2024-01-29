import pandas as pd
from simple_salesforce import Salesforce


def main():
    username = ''
    password = ''
    security_token = ''

    sf = Salesforce(username=username, password=password, security_token=security_token)
    fieldname = 'FIELDS(ALL)'
    objectname = 'Lead'  # Account, Campaign, Case, Contact, Lead
    limit = 5  # max_limit = 200
    offset = 0
    data = []

    run = True
    while run:
        query = f"""SELECT {fieldname} FROM {objectname}
                    LIMIT {limit}
                    OFFSET {offset}"""

        response = sf.query_all(query)
        totalSize = response['totalSize']

        for record in response['records']:
            data.append(record)

        if totalSize == limit:
            run = True
            offset += limit
        else:
            run = False

    pd.json_normalize(data).to_csv(f'./sample/{objectname}.csv', index=False)


if __name__ == "__main__":
    main()
