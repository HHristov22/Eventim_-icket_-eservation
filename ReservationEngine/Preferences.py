class Preferences:
    def __init__(self, filename):
        self.filename = filename    
        
    def createUserPreferencesList(self):
        try:
            fileWithUserPrefs = open(self.filename, "r", encoding='utf-8-sig')
            lines = fileWithUserPrefs.readlines()
            fileWithUserPrefs.close()
            
            tempList = []
            for line in lines:
                line = line.split(',')
                line = [i.strip() for i in line]
                tempList.append(line)
            
            return tempList
            # (tempList[0] = types, tempList[1] = dates, tempList[2] = times, tempList[3] = numberOfTickets, tempList[4] = priceRange) 
        except IOError as e:
            print("Error opening the preferences file:", str(e))
            return []
