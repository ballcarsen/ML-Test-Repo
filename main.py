import helpers.say.hello as hello
import helpers.say.midway as midway
import helpers.say.goodbye as goodbye
import helpers.classFile as classFile

print("running main")

hello.run()
midway.run()
goodbye.run()

classInstance = classFile.simpleClass(str(99))
classInstance.classMethod();