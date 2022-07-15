from auto_factory import AutoFactory

factory = AutoFactory()

for carname in 'Volt', 'Ford', 'Jeep', 'Tesla':
    car = factory.create_instance(carname)
    car.start()
    car.stop()
