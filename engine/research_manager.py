class ResearchManager:

    @staticmethod
    def update(government):

        progress = government.research_progress

        if progress >= 25 and not government.rapid_testing:

            government.rapid_testing = True

            return "Rapid Testing"

        if progress >= 50 and not government.better_treatment:

            government.better_treatment = True

            return "Better Treatment"

        if progress >= 75 and not government.vaccine_prototype:

            government.vaccine_prototype = True

            return "Vaccine Prototype"

        if progress >= 100 and not government.vaccine_unlocked:

            government.vaccine_unlocked = True

            return "Vaccine"

        return None