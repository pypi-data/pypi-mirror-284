import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw
from q_learning_duopoly_logit import LogitCollusionEnv, LogitCollusionLearner
from q_learning_duopoly_linear import LinearCollusionEnv, LinearCollusionLearner
from q_learning_duopoly_hotelling import HotellingCollusionEnv, HotellingCollusionLearner

# Define demand functions
def logit_demand(own_price, other_prices, own_quality, other_qualities, mu, outside_quality):
    other_terms = np.sum(np.exp((other_qualities - other_prices) / mu))
    return np.exp((own_quality - own_price) / mu) / (np.exp(outside_quality / mu) + np.exp((own_quality - own_price) / mu) + other_terms)

def hotelling_demand(own_price, other_price, own_quality, other_quality, theta):
    return 0.5 + 0.5 * (own_quality - own_price - other_quality + other_price) / theta

def linear_demand(own_price, other_price, own_quality,other_quality,  b, d):
    return (b*(own_quality - own_price) - d*(other_quality - other_price)) / (b**2 - d**2)

# Nash Equilibrium Solvers
def hotelling_nash(qualities, costs, theta):
    prices = [theta + (qualities[i]-qualities[1-i] + 2*costs[i]+costs[1-i])/3 for i in range(len(costs))]
    return prices

def linear_nash(qualities, costs, b, d):
    prices = [ ((2*b**2-d**2)*qualities[i]+2*b**2*costs[i]+b*d*costs[1-i]-b*d*qualities[1-i])/(4*b**2-d**2) for i in range(len(costs))]
    return prices

def logit_fixed_point(c, a, outside_quality, mu, tol=1e-10, max_iter=1000):
    c, a = np.array(c), np.array(a)
    p = np.array(c)
    for i in range(max_iter):
        next_p = np.array([c[i] + mu * (1 + lambertw(np.exp((a[i] - c[i] - mu) / mu) / (np.exp(outside_quality / mu) + np.sum([np.exp((a[j] - p[j]) / mu) for j in range(len(c)) if j != i]))).real) for i in range(len(c))])
        if np.allclose(p, next_p, atol=tol):
            return next_p
        p = next_p
    return p

# Define profit and best price functions
def profit(price, demand, cost):
    return (price - cost) * demand

def logit_best_price(prices, other_prices, quality, other_qualities, mu, outside_quality, cost):
    profits = []
    for price in prices:
        current_demand = logit_demand(price, other_prices, quality, other_qualities, mu, outside_quality)
        current_profit = profit(price, current_demand, cost)
        profits.append(current_profit)
    return prices[np.argmax(profits)]

def hotelling_best_price(prices, other_prices, quality, other_qualities, theta, cost):
    profits = []
    for price in prices:
        current_demand = hotelling_demand(price, other_prices, quality, other_qualities, theta)
        current_profit = profit(price, current_demand, cost)
        profits.append(current_profit)
    return prices[np.argmax(profits)]

def linear_best_price(prices, other_prices, quality, other_qualities, b,d, cost):
    profits = []
    for price in prices:
        current_demand = linear_demand(price, other_prices, quality, other_qualities, b,d)
        current_profit = profit(price, current_demand, cost)
        profits.append(current_profit)
    return prices[np.argmax(profits)]

# Define PSO algorithm
def logit_pso_simulation_firms(num_firms, quality, mu, outside_quality, cost, shock, **kwargs): 
    num_particles = kwargs.get('num_particles', 5)
    num_iterations = kwargs.get('num_iterations', 1000)
    seed = kwargs.get('seed', 1)
    w0 = kwargs.get('w0', 0.025)
    self_confidence = kwargs.get('self_confidence', 1.75)
    social_confidence = kwargs.get('social_confidence', 1.75)
    v_min = kwargs.get('v_min', -0.3)
    v_max = kwargs.get('v_max', 0.3)
    memory_size = kwargs.get('memory_size', 5)
    hilp_iteration = kwargs.get('hilp_iteration', 500)
    shock_size = kwargs.get('shock_size', 0.5)
    price_jump = shock_size if shock else 0

    prices_over_iterations = [[] for _ in range(num_firms)]
    np.random.seed(seed)
    prices = [np.random.uniform(0, 1, num_particles) for _ in range(num_firms)]
    velocities = [np.zeros(num_particles) for _ in range(num_firms)]
    for i in range(num_firms):
        prices_over_iterations[i].append(prices[i].copy())
    pbest_memory = [[[] for _ in range(num_particles)] for _ in range(num_firms)]
    pbest_profits_memory = [[[] for _ in range(num_particles)] for _ in range(num_firms)]
    for j in range(num_firms):
        for i in range(num_particles):
            other_prices = np.delete(prices, j, axis=0)
            other_qualities = np.delete(quality, j)
            current_demand = logit_demand(prices[j][i], other_prices[:, i], quality[j], other_qualities, mu, outside_quality)
            current_profit = profit(prices[j][i], current_demand, cost[j])
            pbest_memory[j][i].append(prices[j][i])
            pbest_profits_memory[j][i].append(current_profit)
    gbest_memory = [[] for _ in range(num_firms)]
    gbest_profits_memory = [[] for _ in range(num_firms)]
    for j in range(num_firms):
        gbest_memory[j].append(logit_best_price(prices[j], np.delete(prices, j, axis=0)[:, 0], quality[j], np.delete(quality, j), mu, outside_quality, cost[j]))
        gbest_profits_memory[j].append(profit(gbest_memory[j][0], logit_demand(gbest_memory[j][0], np.delete(prices, j, axis=0)[:, 0], quality[j], np.delete(quality, j), mu, outside_quality), cost[j]))
    for iteration in range(num_iterations):
        if iteration == hilp_iteration:
            for j in range(num_firms):
                for i in range(num_particles):
                    prices[j][i] += price_jump
        w = (1 - w0) ** iteration
        for j in range(num_firms):
            for i in range(num_particles):
                r1, r2 = np.random.uniform(0, 1, 2)
                other_prices = np.delete(prices, j, axis=0)
                other_qualities = np.delete(quality, j)
                velocities[j][i] = np.clip(
                    w * velocities[j][i] +
                    self_confidence * r1 * (max(pbest_memory[j][i], key=lambda p: profit(p, logit_demand(p, other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j])) - prices[j][i]) +
                    social_confidence * r2 * (max(gbest_memory[j], key=lambda p: profit(p, logit_demand(p, other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j])) - prices[j][i]),
                    v_min, v_max)
                prices[j][i] += velocities[j][i]
        for i in range(num_firms):
            prices_over_iterations[i].append(prices[i].copy())
        for j in range(num_firms):
            for i in range(num_particles):
                other_prices = np.delete(prices, j, axis=0)
                other_qualities = np.delete(quality, j)
                current_profit = profit(prices[j][i], logit_demand(prices[j][i], other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j])
                pbest_memory[j][i].append(prices[j][i])
                pbest_profits_memory[j][i].append(current_profit)
                if len(pbest_memory[j][i]) > memory_size:
                    pbest_memory[j][i].pop(0)
                    pbest_profits_memory[j][i].pop(0)
            if len(gbest_memory[j]) >= memory_size:
                gbest_memory[j].pop(0)
                gbest_profits_memory[j].pop(0)
            max_pbest = max([max(p, key=lambda p: profit(p, logit_demand(p, other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j])) for p in pbest_memory[j]], key=lambda p: profit(p, logit_demand(p, other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j]))
            gbest_memory[j].append(max_pbest)
            max_gbest_profit = max([max(p, key=lambda p: profit(p, logit_demand(p, other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j])) for p in pbest_memory[j]], key=lambda p: profit(p, logit_demand(p, other_prices[:, i], quality[j], other_qualities, mu, outside_quality), cost[j]))
            gbest_profits_memory[j].append(max_gbest_profit)
    return prices_over_iterations

def hotelling_pso_simulation_firms(quality ,theta, cost, shock, **kwargs): 
    num_particles = kwargs.get('num_particles', 5)
    num_iterations = kwargs.get('num_iterations', 1000)
    seed = kwargs.get('seed', 1)
    w0 = kwargs.get('w0', 0.025)
    self_confidence = kwargs.get('self_confidence', 1.75)
    social_confidence = kwargs.get('social_confidence', 1.75)
    v_min = kwargs.get('v_min', -0.3)
    v_max = kwargs.get('v_max', 0.3)
    memory_size = kwargs.get('memory_size', 5)
    hilp_iteration = kwargs.get('hilp_iteration', 500)
    shock_size = kwargs.get('shock_size', 0.5)
    price_jump = shock_size if shock else 0

    prices_over_iterations = [[] for _ in range(2)]
    np.random.seed(seed)
    prices = [np.random.uniform(0, 1, num_particles) for _ in range(2)]
    velocities = [np.zeros(num_particles) for _ in range(2)]
    for i in range(2):
        prices_over_iterations[i].append(prices[i].copy())
    pbest_memory = [[[] for _ in range(num_particles)] for _ in range(2)]
    pbest_profits_memory = [[[] for _ in range(num_particles)] for _ in range(2)]
    for j in range(2):
        for i in range(num_particles):
            other_prices = np.delete(prices, j, axis=0)
            other_qualities = np.delete(quality, j)
            current_demand = hotelling_demand(prices[j][i], other_prices[:, i], quality[j], other_qualities, theta)
            current_profit = profit(prices[j][i], current_demand, cost[j])
            pbest_memory[j][i].append(prices[j][i])
            pbest_profits_memory[j][i].append(current_profit)
    gbest_memory = [[] for _ in range(2)]
    gbest_profits_memory = [[] for _ in range(2)]
    for j in range(2):
        gbest_memory[j].append(hotelling_best_price(prices[j], np.delete(prices, j, axis=0)[:, 0], quality[j], np.delete(quality, j), theta, cost[j]))
        gbest_profits_memory[j].append(profit(gbest_memory[j][0], hotelling_demand(gbest_memory[j][0], np.delete(prices, j, axis=0)[:, 0], quality[j], np.delete(quality, j), theta), cost[j]))
    for iteration in range(num_iterations):
        if iteration == hilp_iteration:
            for j in range(2):
                for i in range(num_particles):
                    prices[j][i] += price_jump
        w = (1 - w0) ** iteration
        for j in range(2):
            for i in range(num_particles):
                r1, r2 = np.random.uniform(0, 1, 2)
                other_prices = np.delete(prices, j, axis=0)
                other_qualities = np.delete(quality, j)
                velocities[j][i] = np.clip(
                    w * velocities[j][i] +
                    self_confidence * r1 * (max(pbest_memory[j][i], key=lambda p: profit(p, hotelling_demand(p, other_prices[:, i], quality[j], other_qualities, theta), cost[j])) - prices[j][i]) +
                    social_confidence * r2 * (max(gbest_memory[j], key=lambda p: profit(p, hotelling_demand(p, other_prices[:, i], quality[j], other_qualities,theta), cost[j])) - prices[j][i]),
                    v_min, v_max)
                prices[j][i] += velocities[j][i]
        for i in range(2):
            prices_over_iterations[i].append(prices[i].copy())
        for j in range(2):
            for i in range(num_particles):
                other_prices = np.delete(prices, j, axis=0)
                other_qualities = np.delete(quality, j)
                current_profit = profit(prices[j][i], hotelling_demand(prices[j][i], other_prices[:, i], quality[j], other_qualities, theta), cost[j])
                pbest_memory[j][i].append(prices[j][i])
                pbest_profits_memory[j][i].append(current_profit)
                if len(pbest_memory[j][i]) > memory_size:
                    pbest_memory[j][i].pop(0)
                    pbest_profits_memory[j][i].pop(0)
            if len(gbest_memory[j]) >= memory_size:
                gbest_memory[j].pop(0)
                gbest_profits_memory[j].pop(0)
            max_pbest = max([max(p, key=lambda p: profit(p, hotelling_demand(p, other_prices[:, i], quality[j], other_qualities, theta), cost[j])) for p in pbest_memory[j]], key=lambda p: profit(p, hotelling_demand(p, other_prices[:, i], quality[j], other_qualities, theta), cost[j]))
            gbest_memory[j].append(max_pbest)
            max_gbest_profit = max([max(p, key=lambda p: profit(p, hotelling_demand(p, other_prices[:, i], quality[j], other_qualities, theta), cost[j])) for p in pbest_memory[j]], key=lambda p: profit(p, hotelling_demand(p, other_prices[:, i], quality[j], other_qualities, theta), cost[j]))
            gbest_profits_memory[j].append(max_gbest_profit)
    return prices_over_iterations

def linear_pso_simulation_firms(quality ,b,d, cost, shock, **kwargs): 
    num_particles = kwargs.get('num_particles', 5)
    num_iterations = kwargs.get('num_iterations', 1000)
    seed = kwargs.get('seed', 1)
    w0 = kwargs.get('w0', 0.025)
    self_confidence = kwargs.get('self_confidence', 1.75)
    social_confidence = kwargs.get('social_confidence', 1.75)
    v_min = kwargs.get('v_min', -0.3)
    v_max = kwargs.get('v_max', 0.3)
    memory_size = kwargs.get('memory_size', 5)
    hilp_iteration = kwargs.get('hilp_iteration', 500)
    shock_size = kwargs.get('shock_size', 0.5)
    price_jump = shock_size if shock else 0

    prices_over_iterations = [[] for _ in range(2)]
    np.random.seed(seed)
    prices = [np.random.uniform(0, 1, num_particles) for _ in range(2)]
    velocities = [np.zeros(num_particles) for _ in range(2)]
    for i in range(2):
        prices_over_iterations[i].append(prices[i].copy())
    pbest_memory = [[[] for _ in range(num_particles)] for _ in range(2)]
    pbest_profits_memory = [[[] for _ in range(num_particles)] for _ in range(2)]
    for j in range(2):
        for i in range(num_particles):
            other_prices = np.delete(prices, j, axis=0)
            other_qualities = np.delete(quality, j)
            current_demand = linear_demand(prices[j][i], other_prices[:, i], quality[j], other_qualities, b,d)
            current_profit = profit(prices[j][i], current_demand, cost[j])
            pbest_memory[j][i].append(prices[j][i])
            pbest_profits_memory[j][i].append(current_profit)
    gbest_memory = [[] for _ in range(2)]
    gbest_profits_memory = [[] for _ in range(2)]
    for j in range(2):
        gbest_memory[j].append(linear_best_price(prices[j], np.delete(prices, j, axis=0)[:, 0], quality[j], np.delete(quality, j), b,d, cost[j]))
        gbest_profits_memory[j].append(profit(gbest_memory[j][0], linear_demand(gbest_memory[j][0], np.delete(prices, j, axis=0)[:, 0], quality[j], np.delete(quality, j), b,d), cost[j]))
    for iteration in range(num_iterations):
        if iteration == hilp_iteration:
            for j in range(2):
                for i in range(num_particles):
                    prices[j][i] += price_jump
        w = (1 - w0) ** iteration
        for j in range(2):
            for i in range(num_particles):
                r1, r2 = np.random.uniform(0, 1, 2)
                other_prices = np.delete(prices, j, axis=0)
                other_qualities = np.delete(quality, j)
                velocities[j][i] = np.clip(
                    w * velocities[j][i] +
                    self_confidence * r1 * (max(pbest_memory[j][i], key=lambda p: profit(p, linear_demand(p, other_prices[:, i], quality[j], other_qualities, b,d), cost[j])) - prices[j][i]) +
                    social_confidence * r2 * (max(gbest_memory[j], key=lambda p: profit(p, linear_demand(p, other_prices[:, i], quality[j], other_qualities,b,d), cost[j])) - prices[j][i]),
                    v_min, v_max)
                prices[j][i] += velocities[j][i]
        for i in range(2):
            prices_over_iterations[i].append(prices[i].copy())
        for j in range(2):
            for i in range(num_particles):
                other_prices = np.delete(prices, j, axis=0)
                other_qualities = np.delete(quality, j)
                current_profit = profit(prices[j][i], linear_demand(prices[j][i], other_prices[:, i], quality[j], other_qualities, b,d), cost[j])
                pbest_memory[j][i].append(prices[j][i])
                pbest_profits_memory[j][i].append(current_profit)
                if len(pbest_memory[j][i]) > memory_size:
                    pbest_memory[j][i].pop(0)
                    pbest_profits_memory[j][i].pop(0)
            if len(gbest_memory[j]) >= memory_size:
                gbest_memory[j].pop(0)
                gbest_profits_memory[j].pop(0)
            max_pbest = max([max(p, key=lambda p: profit(p, linear_demand(p, other_prices[:, i], quality[j], other_qualities, b,d), cost[j])) for p in pbest_memory[j]], key=lambda p: profit(p, linear_demand(p, other_prices[:, i], quality[j], other_qualities, b,d), cost[j]))
            gbest_memory[j].append(max_pbest)
            max_gbest_profit = max([max(p, key=lambda p: profit(p, linear_demand(p, other_prices[:, i], quality[j], other_qualities, b,d), cost[j])) for p in pbest_memory[j]], key=lambda p: profit(p, linear_demand(p, other_prices[:, i], quality[j], other_qualities, b,d), cost[j]))
            gbest_profits_memory[j].append(max_gbest_profit)
    return prices_over_iterations


# Define logit PSO for n firms function

def logit_pso(costs, qualities, outside_quality, mu, num_firms, shock, seed, plot, **kwargs):
    nash_prices = logit_fixed_point(costs, qualities, outside_quality, mu)
    prices_over_iterations = logit_pso_simulation_firms(num_firms, qualities, mu, outside_quality, costs, shock, seed=seed, **kwargs)

    # Print final and Nash prices
    for j in range(num_firms):
        final_prices = np.array([prices_over_iterations[j][-1][i] for i in range(kwargs.get('num_particles', 5))])
        average_final_price = np.mean(final_prices)
        print(f"Firm {j+1} PSO: {average_final_price:.4f}, Nash: {nash_prices[j]:.4f}")

    # Optional plotting
    if plot:
        plt.figure(figsize=(10, 6))
        for j in range(num_firms):
            prices_array = np.array(prices_over_iterations[j]).T
            for i in range(kwargs.get('num_particles', 5)):
                plt.plot(prices_array[i], label=f'Firm {j+1} Particle {i+1}', linestyle='-')
            plt.axhline(y=nash_prices[j], color='red', linestyle='-', linewidth=1, label=f'Firm {j+1} Nash Equilibrium')
        plt.xlabel('Iteration')
        plt.ylabel('Price')
        plt.legend()
        plt.title('Prices Over Iterations for Multiple Firms')
        plt.show()

# Define logit_duopoly function

def logit_duopoly(costs, qualities, outside_quality, mu, algorithm, seed, plot, shock, **kwargs):
    # Calculate Nash prices
    nash_prices = logit_fixed_point(costs, qualities, outside_quality, mu)

    if algorithm.lower() == 'pso':
        prices_over_iterations = logit_pso_simulation_firms(2, qualities, mu, outside_quality, costs, shock, seed=seed, **kwargs)

        for j in range(2):
            final_prices = np.array([prices_over_iterations[j][-1][i] for i in range(kwargs.get('num_particles', 5))])
            average_final_price = np.mean(final_prices)
            print(f"Firm {j+1} PSO: {average_final_price:.4f}, Nash: {nash_prices[j]:.4f}")
        
        if plot:
            plt.figure(figsize=(10, 6))
            for j in range(2):
                prices_array = np.array(prices_over_iterations[j]).T
                for i in range(kwargs.get('num_particles', 5)):
                    plt.plot(prices_array[i], label=f'Firm {j+1} Particle {i+1}', linestyle='-')
                plt.axhline(y=nash_prices[j], color='red', linestyle='-', linewidth=1, label=f'Nash price for Firm {j+1}')
            plt.xlabel('Iteration')
            plt.ylabel('Price')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.title('Logit Prices Over Iterations for Two Firms')
            plt.show()

    elif algorithm.lower() in ['q', 'q-learning', 'qlearning', 'q_learning', 'qlearning']:
        # Set up the Q-learning environment and learners
        num_possible_actions = kwargs.get('num_possible_actions', 15)
        num_possible_states = num_possible_actions ** 2
        
        # Initialize agents with qualities and costs
        agent1 = LogitCollusionLearner(num_possible_actions, num_possible_states, nash_prices, **kwargs)
        agent2 = LogitCollusionLearner(num_possible_actions, num_possible_states, nash_prices, **kwargs)
        
        # Update agent parameters with given inputs
        agent1.a_i, agent2.a_i = qualities
        agent1.c_i, agent2.c_i = costs
        agent1.a_0 = agent2.a_0 = outside_quality
        agent1.mu = agent2.mu = mu
        
        agents = [agent1, agent2]
        
        # Create the environment
        env = LogitCollusionEnv(agents, num_possible_actions, num_possible_states, nash_prices, seed=seed, shock=shock, **kwargs)
        
        # Run the environment
        env.run()
        
        # Print final and Nash prices
        final_prices = [agent1.action_price_space[agent1.my_action_hist[-1]], agent2.action_price_space[agent2.my_action_hist[-1]]]
        for j in range(2):
            print(f"Firm {j+1} Q-learning: {final_prices[j]:.4f}, Nash: {nash_prices[j]:.4f}")

    else:
        return ValueError('Invalid algorithm')




    
def hotelling_duopoly(costs, qualities, theta, algorithm, seed, plot, shock, **kwargs):
    # Calculate Nash prices
    nash_prices = hotelling_nash(qualities, costs, theta)

    if algorithm.lower() == 'pso':
        prices_over_iterations = hotelling_pso_simulation_firms(qualities, theta, costs, shock, seed=seed, **kwargs)

        for j in range(2):
            final_prices = np.array([prices_over_iterations[j][-1][i] for i in range(kwargs.get('num_particles', 5))])
            average_final_price = np.mean(final_prices)
            print(f"Firm {j+1} PSO: {average_final_price:.4f}, Nash: {nash_prices[j]:.4f}")
        
        if plot:
            plt.figure(figsize=(10, 6))
            for j in range(2):
                prices_array = np.array(prices_over_iterations[j]).T
                for i in range(kwargs.get('num_particles', 5)):
                    plt.plot(prices_array[i], label=f'Firm {j+1} Particle {i+1}', linestyle='-')
                plt.axhline(y=nash_prices[j], color='red', linestyle='-', linewidth=1, label=f'Nash price for Firm {j+1}')
            plt.xlabel('Iteration')
            plt.ylabel('Price')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.title('Hotelling Prices Over Iterations for Two Firms')
            plt.show()

    elif algorithm.lower() in ['q', 'q-learning', 'qlearning', 'q_learning', 'qlearning']:
        # Set up the Q-learning environment and learners
        num_possible_actions = kwargs.get('num_possible_actions', 15)
        num_possible_states = num_possible_actions ** 2
        
        # Initialize agents with qualities and costs
        agent1 = HotellingCollusionLearner(num_possible_actions, num_possible_states, nash_prices, **kwargs)
        agent2 = HotellingCollusionLearner(num_possible_actions, num_possible_states, nash_prices, **kwargs)
        
        # Update agent parameters with given inputs
        agent1.a_i, agent2.a_i = qualities
        agent1.c_i, agent2.c_i = costs
        agent1.theta = agent2.theta = theta
        
        agents = [agent1, agent2]
        
        # Create the environment
        env = HotellingCollusionEnv(agents, num_possible_actions, num_possible_states, nash_prices, seed=seed, shock=shock, **kwargs)
        
        # Run the environment
        env.run()
        
        # Print final and Nash prices
        final_prices = [agent1.action_price_space[agent1.my_action_hist[-1]], agent2.action_price_space[agent2.my_action_hist[-1]]]
        for j in range(2):
            print(f"Firm {j+1} Q-learning: {final_prices[j]:.4f}, Nash: {nash_prices[j]:.4f}")

    else:
        return ValueError('Invalid algorithm')


def linear_duopoly(costs, qualities, b, d, algorithm, seed, plot, shock, **kwargs):
    # Calculate Nash prices
    nash_prices = linear_nash(qualities, costs, b, d)

    if algorithm.lower() == 'pso':
        prices_over_iterations = linear_pso_simulation_firms(qualities, b, d, costs, shock, seed=seed, **kwargs)

        for j in range(2):
            final_prices = np.array([prices_over_iterations[j][-1][i] for i in range(kwargs.get('num_particles', 5))])
            average_final_price = np.mean(final_prices)
            print(f"Firm {j+1} PSO: {average_final_price:.4f}, Nash: {nash_prices[j]:.4f}")
        
        if plot:
            plt.figure(figsize=(10, 6))
            for j in range(2):
                prices_array = np.array(prices_over_iterations[j]).T
                for i in range(kwargs.get('num_particles', 5)):
                    plt.plot(prices_array[i], label=f'Firm {j+1} Particle {i+1}', linestyle='-')
                plt.axhline(y=nash_prices[j], color='red', linestyle='-', linewidth=1, label=f'Nash price for Firm {j+1}')
            plt.xlabel('Iteration')
            plt.ylabel('Price')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.title('Linear Prices Over Iterations for Two Firms')
            plt.show()

    elif algorithm.lower() in ['q', 'q-learning', 'qlearning', 'q_learning', 'qlearning']:
        # Set up the Q-learning environment and learners
        num_possible_actions = kwargs.get('num_possible_actions', 15)
        num_possible_states = num_possible_actions ** 2
        
        # Initialize agents with qualities and costs
        agent1 = LinearCollusionLearner(num_possible_actions, num_possible_states, nash_prices, **kwargs)
        agent2 = LinearCollusionLearner(num_possible_actions, num_possible_states, nash_prices, **kwargs)
        
        # Update agent parameters with given inputs
        agent1.a_i, agent2.a_i = qualities
        agent1.c_i, agent2.c_i = costs
        agent1.b = agent2.b = b
        agent1.d = agent2.d = d
        
        agents = [agent1, agent2]
        
        # Create the environment
        env = LinearCollusionEnv(agents, num_possible_actions, num_possible_states, nash_prices, seed=seed, shock=shock, **kwargs)
        
        # Run the environment
        env.run()
        
        # Print final and Nash prices
        final_prices = [agent1.action_price_space[agent1.my_action_hist[-1]], agent2.action_price_space[agent2.my_action_hist[-1]]]
        for j in range(2):
            print(f"Firm {j+1} Q-learning: {final_prices[j]:.4f}, Nash: {nash_prices[j]:.4f}")

    else:
        return ValueError('Invalid algorithm')
