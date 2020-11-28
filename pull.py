def find_mine():
    big_dic = {
        "city":{
            "arusha":{
                "rural":{
                    "mbauda":{
                        "sombetini"
                    }
                },
                "urban":{
                    "morombo":{
                        "ngalelo"
                    }
                }
            }
            
        }
    }

    print(big_dic["city"]["arusha"].keys())
    # big_dic[city][city_names[0]][urb_rur[0]][street[]][ward]
find_mine()