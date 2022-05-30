def algorithm_results(logger, algo_name, explorer, found_goal, goal_state):
    if found_goal:
        logger.info(f"Finished {algo_name} run. Found goal.")
        return explorer.steps_to_state(goal_state), explorer.statistics()
    else:
        logger.info("Finished {algo_name} run. Did not find goal.")
        return None, explorer.statistics()
