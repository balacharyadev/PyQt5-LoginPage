# PyQt5-LoginPage
using PyQt5, MongoDB. 

**Basic Features———✔**.

       ¬Options Page
   
       ¬User validation
   
       ¬Email Validation
   
       ¬Establish with MongoDB-Community

**Run Programe———✔**.

       ¬pip.__version__ >= 20 ( otherversions not supported )
   
       ¬__init__.py 👉 Run as administrator (internet is helpful, because requirements.txt is automatically installed)
   
       ¬Then auto-launching the GUI
   
       ( 💨HINT ::> 

       from mainpage.py,

               self.con = MongoClient("mongodb://127.0.0.1:27017")
               self.db = self.con['PYQT5-LOGINPAGE']
               self.col = self.db['USERS'] 

       To Change, 

              ==> "mongodb://127.0.0.1:27017" ==> Your Server address
              ==> 'PYQT5-LOGINPAGE' ==> Your db name
              ==> 'USERS' ==> Your collection name
              
       )

**Run and enjoy** ❤💥
  
