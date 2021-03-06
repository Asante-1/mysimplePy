class Motor(object):
    Company = 'Duccatti motors'

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year  = year
        self.odometer_reading = 0
        
    @classmethod
    def company_name(cls):
        print(cls.Company)

    def motor_name(self):
        print('name : ', self.name)
        print('model :', self.model)
        print('year :' , self.year)


    def odometer_read(self):
        print('The motor has ', self.odometer_reading,'miles on it')

    def update_odometer(self, mileage):
        if mileage >= int(self.odometer_reading):
            self.odometer_reading = mileage
        else:
            print("You cannot rollback the odometer")



    def distance_travelled(self, miles):
        self.odometer_reading += miles
        print("Distance travelled", self.odometer_reading,'\n\n')

class Electri_motor(Motor):
    def __init__(self, name, model, year):
        super(). __init__(name, model, year)

    def company_name(cls):
        print(cls.Company)

    def elec_motorname(self):
        super().motor_name()


    def travelled(self):
        super().distance_travelled(50)




now = Electri_motor('metyhal', '2_heat', 2020)
now.company_name()
now.elec_motorname()
now.travelled()







motor = Motor('Merisha', '1z', 2019)
motor.company_name()
motor.motor_name()
motor.odometer_read()
motor.update_odometer(5)
motor.distance_travelled(7

