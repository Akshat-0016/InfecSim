class ActivePolicy:

    def __init__(self, policy):

        self.policy = policy
        self.remaining_days = policy.duration