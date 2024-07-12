def содержит(что, где, игнорироввать_регистр=False):
    if что == "" or где == "":
        raise ValueError("нельзя передавать пустые значения")
    if (type(что) != list and type(что) != str) or (type(где) != list and type(где) != str):
        raise ValueError("можно передавать только списки и текст")
    if type(что) == list:
        for элемент in что:
            if type(элемент) != str:
                raise ValueError("список должен содержать только строковые значения")
    if type(где) == list:
        for элемент in где:
            if type(элемент) != str:
                raise ValueError("список должен содержать только строковые значения")
    
    if игнорироввать_регистр:
        if type(что) == str:
            что = что.lower()
        else:
            без_регистра = []
            for элемент in что:
                без_регистра.append(элемент.lower())
            что = без_регистра          

        if type(где) == str:
            где = где.lower()
        else:
            без_регистра = []
            for элемент in где:
                без_регистра.append(элемент.lower())
            где = без_регистра          





    
        
    
    
    if type(что) == type(где) == str:
        return что in где

    if type(что) == list and type(где) == str:
        for элемент in что:
            if элемент in где:
                return True


    if type(что) == str and type(где) == list:
        for элемент in  где:
            if  что in элемент:
                return True
            
    if type(что) == type(где) == list:
        for элемент_что in что:
            for элемент_где in где:
                if элемент_что in элемент_где:
                    return True 
                
        

    return False

if __name__ == "__main__":
    print(содержит(что=["А","Б"], где=["АБВ", "где"]))

