class ModelBasedReflexAgent:

    def __init__(self):
        self.previous_action = None

    def act(self, temperature):

        if temperature < 20:
            action = "Turn Heater ON"

        elif temperature > 25:
            action = "Turn Heater OFF"

        else:
            action = "Do Nothing"

        if action == self.previous_action:
            action = "Maintain Current State"

        self.previous_action = action
        return action


agent = ModelBasedReflexAgent()

temperatures = [18, 19, 21, 26, 27, 23, 18]

for temp in temperatures:
    action = agent.act(temp)
    print("Temperature:", temp, "→ Action:", action)