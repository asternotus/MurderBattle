from States.State import State

class CleanState(State):

    def clean(self, citizens):
        for citizen in citizens:
            for effect in citizen.effects:
                if(effect == "killed" or effect == "stolen"):
                    citizen.effects.remove(effect)




