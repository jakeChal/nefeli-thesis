from gym import Env
from house import House
from value_iteration import value_iteration
import matplotlib.pyplot as plt
import numpy as np

#TODO 
#check how many episodes I have to run it to have a good estimate
#check the results for different policies
#run 10000 episodes to evaluate policy because there is a stochasticisity 
#next time: priority difference of deterioration rate over time 
#next time : do nothing - evaluate the rewards according to that 


def run_episodes(env: House, policy: list = None, num_episodes: int = 100):
    total_costs_episodes = []

    num_time_steps = env.num_years // env.time_step
    rewards_all_episodes = np.zeros((num_episodes, num_time_steps))
    states_all_episodes = np.zeros((num_episodes, num_time_steps))

    # Run episodes
    for episode in range(num_episodes):
        print("Episode:", episode + 1)
        state = env.reset()
        done = False
        time_idx = 0
        total_cost = 0
        rewards_current_episode = np.zeros(num_time_steps)
        states_current_episode = np.zeros(num_time_steps)
        while not done:
            if policy is None:
                action = env.action_space.sample()  # Random action for demonstration
            else:
                action = policy[state]
            next_state, reward, done, _ = env.step(action)
            print(f"\tTime step: {time_idx} --> Current State: {state} | Action: {action} | Next State: {next_state} | Reward: {reward:.2f}")
            total_cost += abs(reward)
            rewards_current_episode[time_idx] = (abs(np.round(reward)))
            states_current_episode[time_idx] = state
            state = next_state
            time_idx += 1

        rewards_all_episodes[episode, :] = rewards_current_episode
        states_all_episodes[episode, :] = states_current_episode
        print("Episode finished.\n")

        total_costs_episodes.append(total_cost)

    return total_costs_episodes, rewards_all_episodes, states_all_episodes


def plot_histogram_comparisons(data1, data2):
    # Create a new figure with 1 row and 2 columns of subplots
    plt.figure(figsize=(10, 5))

    # Plot histogram for data1
    plt.hist(data1, bins='auto', color='blue', alpha=0.7, label='Do-nothing policy')

    # Plot histogram for data2
    plt.hist(data2, bins='auto', color='red', alpha=0.7, label='Optimal policy')

    plt.xlabel("Cost [€]")
    plt.ylabel("Frequency")
    plt.title("Histogram Comparison")
    plt.legend()

    plt.show()


def plot_costs_for_policy(env: House, policy: list, rewards: np.ndarray, states: np.ndarray, plot_title: str):
    actions = {0: 'DN', 1: 'R', 2: 'W', 3: 'C'}
    colors = {'DN': 'black', 'R': 'red', 'W': 'green', 'C': 'blue'}
    # labels = {'DN': 'do nothing', 'R': 'roof', 'W': 'wall', 'C': 'cellar'}

    time_axis = np.arange(0, env.num_years, env.time_step)
    plt.plot(time_axis, rewards, marker='o', linestyle='-')
    for i, (xi, yi) in enumerate(zip(time_axis, rewards)):
        string = actions[policy[i]]
        plt.text(xi, yi, string, color=colors[string], weight='bold', ha='center', va='bottom')

    for i, (xi, yi) in enumerate(zip(time_axis, rewards)):
        string = str(int(states[i]))
        plt.text(xi, yi, string, weight='bold', ha='right', va='top')

    plt.ylabel("Costs [€]")
    plt.xlabel("Years")
    plt.title(f"{plot_title} policy")

    plt.grid()
    plt.show()


if __name__ == "__main__":

    env = House()
    zero_policy = [0 for _ in range(env.observation_space.n)] #create a zero policy
    # optimal_policy, optimal_value = value_iteration(env)

    # Evaluate "do-nothing" policy
    total_costs_zero_policy, rewards_all_episodes_zero_policy, states_all_episodes_zero_policy = run_episodes(env=env, policy=zero_policy, num_episodes=100)  # run the zero policy

    # plot costs/policy/states for 1st episode
    plot_costs_for_policy(env, zero_policy, rewards_all_episodes_zero_policy[0], states_all_episodes_zero_policy[0], plot_title='"Do nothing"')
    #total_costs_random_policy = run_episodes(env=env, policy=None) #run a random policy

    # Evaluate using value iteration
    env.reset()
    optimal_policy, optimal_value, num_iterations = value_iteration(env)
    total_costs_value_iteration, rewards_all_episodes_value_iteration, states_all_episodes_value_iteration = run_episodes(env=env, policy=optimal_policy, num_episodes=100)

    # plot costs/policy/states for 1st episode
    plot_costs_for_policy(env, optimal_policy, rewards_all_episodes_value_iteration[0], states_all_episodes_value_iteration[0], plot_title='Value Iteration')

    print(f"Number of iterations for optimal policy: {num_iterations}")
    plot_histogram_comparisons(total_costs_zero_policy, total_costs_value_iteration)

