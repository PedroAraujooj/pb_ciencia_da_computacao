import dns.resolver


if __name__ == '__main__':
    try:
        records = ['A', 'MX', 'NS']
        for record in records:
            try:
                responses = dns.resolver.resolve("example.com", record)
                print('\n Registros', record)
                for response in responses:
                    print(f'       {response}')
            except Exception as e:
                print("Canot resolve query for record ", record)
                print('Error obtaining information: ',e)
    except:
        KeyboardInterrupt: exit()

