from flask import Flask
from flask_restful import Api, Resource
import pandas as pd
import json

data = pd.read_csv('file2.csv',
                   encoding='unicode_escape', engine='python')
app = Flask(__name__)
api = Api(app)


class SaltInformation(Resource):
    def get(self, saltName):
        temp = []
        jj = {}
        # saltName=saltName.upper()
        flag=1
        for i, j in enumerate(data['Generic(Salt) name']):
            if j.upper() == saltName.upper():
                temp = data['Alternatives'][i] + ',' + \
                    data['Medicine(Brand) name'][i]
                temp1=temp.split(",")
                jjj=[]
                for k in range(len(temp1)):
                    temp1[k]=temp1[k].strip()
                    for l,m in enumerate(data['Medicine(Brand) name']):
                        if m==temp1[k]:
                            jjj.append({'name': temp1[k], 'salt':data['Generic(Salt) name'][l] , 'PackageType':data['Package type'][l], 'Price':data['Price(INR)'][l]})
                
                # medicines = []
                # for medicine in temp.split(','):
                #     temp1 = data.loc[data['Medicine(Brand) name'] == medicine]
                #     obj = {'Package type': temp1['Package type'],
                #            'Strength': temp1['Strength'], 'Price': temp1['Price(INR)']}
                #     medicines[temp1['Medicine(Brand) name']] = obj
                jj['name'] = j
                jj['Alternatives'] = jjj
                # jj['list'] = temp
                jj['description'] = data['Description'][i]
                flag=0
                break
        return jj


class MedicineInformation(Resource):
    def get(self, medicineName):
        jj = {}
        medicineName=medicineName.upper()
        for i, j in enumerate(data['Medicine(Brand) name']):
            if j == medicineName:
                jj['name'] = j
                jj['salt'] = data['Generic(Salt) name'][i]
                jj['description']=data['Description'][i]
                jj['Strength']=data['Strength'][i]
                jj['PackageType'] = data['Package type'][i]
                jj['Price'] = data['Price(INR)'][i]
                temp=data['Alternatives'][i]
                temp1=temp.split(",")
                jjj=[]
                for k in range(len(temp1)):
                    temp1[k]=temp1[k].strip()
                    for l,m in enumerate(data['Medicine(Brand) name']):
                        if m==temp1[k]:
                            jjj.append({'name': temp1[k], 'salt':data['Generic(Salt) name'][l] , 'PackageType':data['Package type'][l], 'Price':data['Price(INR)'][l]})
                jj['Alternatives'] = jjj
                break
        return jj


api.add_resource(SaltInformation, "/saltinformation/<string:saltName>")
api.add_resource(MedicineInformation,
                 "/medicineinformation/<string:medicineName>")


if __name__ == "__main__":
    app.run(debug=True)
