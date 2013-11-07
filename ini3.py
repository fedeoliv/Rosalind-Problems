def get_slice(str_collection):
        values = str_collection.split()
        text = values[0]
        return text[int(values[1]):1 + int(values[2])] + " "  + text[int(values[3]):1 + int(values[4])]
    
if __name__ == "__main__":
    print get_slice("oMaKtllur9DB13opqizY1J4gLurtTYEgrettaKs2p9eoJZPVblP2AtZx82FKNQkZpHiKJEadNSKtyBoYL34gSO5AzhoTQcIBgSvqsaLZQWTmPkPPitXJl5zzwQzpjCaZKkbgJfiKalcinouslcBcTWGWR5I96wYS. 30 36 136 143")
