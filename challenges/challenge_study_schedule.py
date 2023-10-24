def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for entrance, exit in permanence_period:
            if entrance <= target_time <= exit:
                counter += 1
        return counter
    except TypeError:
        return None
