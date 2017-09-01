import helpers.say.hello as hello
import helpers.say.goodbye as goodbye
import helpers.classFile as classFile

print("running main")

hello.run()
goodbye.run()

classInstance = classFile.simpleClass(str(99))
classInstance.classMethod();