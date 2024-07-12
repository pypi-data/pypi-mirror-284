import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.special import lambertw

class LinearCollusionEnv():
    def __init__(self, agents, num_tot_actions, num_tot_states, nash_prices, seed=456, **kwargs) -> None:
        self.agents = agents 
        self.num_tot_actions = num_tot_actions
        self.num_tot_states = num_tot_states
        self.max_steps = kwargs.get('max_steps', 1000000)
        random.seed(seed)
        np.random.seed(seed)
        self.shock = kwargs.get('shock', False)
        self.nash_prices = nash_prices
    
    def run(self): 
        # We generate random prices to provide initial observation to Q learners
        num_tot_actions = self.num_tot_actions
        agents = self.agents
        agent1, agent2 = agents
        random_actions = [random.randint(0, num_tot_actions - 1), random.randint(0, num_tot_actions - 1)]
        agent1.my_action_hist.append(random_actions[0])
        agent1.opp_action_hist.append(random_actions[1])
        agent1.s = agent1.determine_state()
        agent1.choose_next_move(step = 0)
        
        agent2.my_action_hist.append(random_actions[1])
        agent2.opp_action_hist.append(random_actions[0])
        agent2.s = agent2.determine_state()
        agent2.choose_next_move(step = 0)

        actions = np.array([agent1.a, agent2.a])

        step = 0
        while step < self.max_steps:
            # Increment and print step count every 100000 steps
            step += 1
            if step % 100000 == 0:
                print("Steps completed: ", step)

            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            old_states = [agent1.determine_state(), agent2.determine_state()]
            for i, agent in enumerate(agents):
                agent.choose_next_move(step = step)
                actions[i] = agent.a

            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            
            prices = agent1.action_price_space.take(
                actions)  # Convert actions into prices

            # Compute rewards at current prices
            rewards = {}
            for i, agent in enumerate(agents):
                demand_i = (agent.b * (agent.a_i - prices[i]) - agent.d * (agent.a_j - prices[1-i])) / (agent.b**2 - agent.d**2)
                rewards[i] = (prices[i] - agent.c_i) * demand_i

            # Update agents' tables and check convergence a la Johnson et al. 2021
            old_optimal_actions = [
                np.argmax(agents[i].q[:, old_states[i]]) for i in range(2)]
            for i in range(2):
                agents[i].transition(rewards[i], step)
            agent1.my_action_hist.append(agent1.a)
            agent1.opp_action_hist.append(agent2.a)
            agent2.my_action_hist.append(agent2.a)
            agent2.opp_action_hist.append(agent1.a)
            
            has_converged = agent1.check_if_converged(old_optimal_actions, step)

            if has_converged:
                break

        # Generate equilibrium price trajectory
        prices = []

        for _ in range(10):
            for i, agent in enumerate(agents):
                agent.choose_next_move(step = step)
                actions[i] = agent.a
            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            prices.append(agent1.action_price_space.take(actions))

        x = range(len(prices))
        y1 = [price[0] for price in prices]
        y2 = [price[1] for price in prices]

        if not self.shock:
            fig, ax = plt.subplots()
            ax.plot(x, y1, 'o-', label='price_1')
            ax.plot(x, y2, 'o-', label='price_2')
            ax.axhline(y=self.nash_prices[0], color='red', linestyle='--', label='Nash price 1')
            ax.axhline(y=self.nash_prices[1], color='green', linestyle='--', label='Nash price 2')
            ax.legend()
            plt.title("Equilibrium price trajectory")
            plt.show()
        

        # Capture prices before deviation
        prices_before_deviation = prices[-5:]  # last 5 periods before deviation
        
        # Test punishment if both agents deviate to the maximum price
        if self.shock:
            max_price_action = self.num_tot_actions - 1
            actions = [max_price_action, max_price_action]
            agent1.my_action_hist[-1] = actions[0]
            agent2.my_action_hist[-1] = actions[1]
            agent1.opp_action_hist[-1] = actions[1]
            agent2.opp_action_hist[-1] = actions[0]
            prices_after_deviation = []

            for _ in range(10):
                prices_after_deviation.append(agent1.action_price_space.take(actions))
                for i, agent in enumerate(agents):
                    agent.choose_next_move(step)
                    actions[i] = agent.a
                agent1.my_action_hist.append(actions[0])
                agent1.opp_action_hist.append(actions[1])
                agent2.my_action_hist.append(actions[1])
                agent2.opp_action_hist.append(actions[0])

            # Concatenate prices before and after deviation
            combined_prices = prices_before_deviation + prices_after_deviation

            x = range(len(combined_prices))
            y1 = [price[0] for price in combined_prices]
            y2 = [price[1] for price in combined_prices]

            fig, ax = plt.subplots()
            ax.plot(x, y1, 'o-', label='price_1')
            ax.plot(x, y2, 'o-', label='price_2')
            ax.axhline(y=self.nash_prices[0], color='red', linestyle='--', label='Nash price 1')
            ax.axhline(y=self.nash_prices[1], color='green', linestyle='--', label='Nash price 2')
            ax.legend()
            plt.title("Prices Before and After Deviation")
            plt.show()

class LinearCollusionLearner():
    def __init__(self, num_possible_actions, num_possible_states, nash_prices, **kwargs):
        grid_lower_bound = kwargs.get('grid_lower_bound', min(nash_prices) - 0.5)  # default min price is min Nash - 0.1
        grid_upper_bound = kwargs.get('grid_upper_bound', max(nash_prices) + 0.5)  # default max price is max Nash + 1
        self.num_actions  = num_possible_actions  # number of discrete prices (seller's action space)
        self.num_states = num_possible_states

        self.learning_rate = kwargs.get('learning_rate', 0.15)
        self.discount_factor = kwargs.get('discount_factor', 0.95)
        self.beta = kwargs.get('beta', 0.00001)
        self.eps = []
        self.q = np.zeros((num_possible_actions, num_possible_states))
        self.action_price_space = np.linspace(
            grid_lower_bound, grid_upper_bound, self.num_actions)  # price grid
        
        self.a_i = kwargs.get('a_i', 2)  # product quality index
        self.c_i = kwargs.get('c_i', 0)
        self.a_j = kwargs.get('a_j', 2)  # product quality index
        self.c_j = kwargs.get('c_j', 0)
        self.b = kwargs.get('b', 1)  # linear model parameter b
        self.d = kwargs.get('d', 0.25)  # linear model parameter d
        self.max_steps = kwargs.get('max_steps', 1000000)  # control how long simulation takes to run
        
        self.init_q()
        self.my_action_hist = []
        self.opp_action_hist = []
    
    def determine_state(self):
        """Generates a state representation from your agent's and your opponent's action histories."""
        if len(self.my_action_hist) == 0 or len(self.opp_action_hist) == 0:
            return 0
        last_my_action = self.my_action_hist[-1]
        last_opp_action = self.opp_action_hist[-1]
        state = last_my_action * self.num_actions + last_opp_action
        return state
        
    def check_if_converged(self, old_optimal_actions, step):
        """Checks if Q matrices have converged, i.e., if optimal actions do not change for 100000 steps"""
        observation = self.determine_state()
        new_optimal_actions = [np.argmax(self.q[:, observation])]
        action_diff = np.sum(np.absolute(
            np.array(new_optimal_actions) - np.array(old_optimal_actions)))
        q_table_stable = True if action_diff == 0 else False

        has_converged = False
        if step == 1:
            self.convergence_counter = 0
        if q_table_stable:
            self.convergence_counter += 1
        else:
            self.convergence_counter = 0
        if self.convergence_counter == 100000:
            print("Converged: True")
            has_converged = True
            print("Convergence_counter:", self.convergence_counter)
            print("Done: ", has_converged)
            print("-------------------------\n\n\n")

        return has_converged

    def init_q(self):
        """Used to initialize Q tables"""
        for s in range(self.num_states): 
            for a1 in range(self.num_actions): 
                reward = 0
                for a2 in range(self.num_actions):
                    price_i = self.action_price_space[a1]
                    price_j = self.action_price_space[a2]
                    demand_0 = (self.b * (self.a_i - price_i) - self.d * (self.a_j - price_j)) / (self.b**2 - self.d**2)
                    profit_0 = (price_i - self.c_i) * demand_0
                    # Assume all actions by the other agent are uniformly possible
                    reward += profit_0 / self.num_actions
                self.q[a1][s] = float(reward / (1 - self.discount_factor))


    def choose_next_move(self, step=0):
        state = self.determine_state()
        epsilon = np.exp(-1 * self.beta * step)
        self.eps.append(epsilon)
        if random.uniform(0, 1) < epsilon:
            price = random.randint(0, self.num_actions - 1)
        else:
            price = np.argmax(self.q[:, state])
        self.a = price

    def update_rule(self, reward):
        self.q[self.a][self.s] += self.learning_rate * \
            (reward + self.discount_factor *
             np.max(self.q[:, self.s_prime]) - self.q[self.a][self.s])

    def transition(self, my_reward, step):
        self.s_prime = self.determine_state()
        self.update_rule(my_reward)
        self.choose_next_move(step)
        self.s = self.s_prime

class HotellingCollusionEnv():
    def __init__(self, agents, num_tot_actions, num_tot_states, nash_prices, seed=456, **kwargs) -> None:
        self.agents = agents 
        self.num_tot_actions = num_tot_actions
        self.num_tot_states = num_tot_states
        self.max_steps = kwargs.get('max_steps', 1000000)
        random.seed(seed)
        np.random.seed(seed)
        self.shock = kwargs.get('shock', False)
        self.nash_prices = nash_prices
    
    def run(self): 
        # We generate random prices to provide initial observation to Q learners
        num_tot_actions = self.num_tot_actions
        agents = self.agents
        agent1, agent2 = agents
        random_actions = [random.randint(0, num_tot_actions - 1), random.randint(0, num_tot_actions - 1)]
        agent1.my_action_hist.append(random_actions[0])
        agent1.opp_action_hist.append(random_actions[1])
        agent1.s = agent1.determine_state()
        agent1.choose_next_move(step = 0)
        
        agent2.my_action_hist.append(random_actions[1])
        agent2.opp_action_hist.append(random_actions[0])
        agent2.s = agent2.determine_state()
        agent2.choose_next_move(step = 0)

        actions = np.array([agent1.a, agent2.a])

        step = 0
        while step < self.max_steps:
            # Increment and print step count every 100000 steps
            step += 1
            if step % 100000 == 0:
                print("Steps completed: ", step)

            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            old_states = [agent1.determine_state(), agent2.determine_state()]
            for i, agent in enumerate(agents):
                agent.choose_next_move(step = step)
                actions[i] = agent.a

            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            
            prices = agent1.action_price_space.take(
                actions)  # Convert actions into prices

            # Compute rewards at current prices
            rewards = {}
            for i, agent in enumerate(agents):
                demand_i = 0.5 + (agent.a_i - prices[i] - agent.a_j + prices[1-i]) / (2 * agent.theta)
                rewards[i] = (prices[i] - agent.c_i) * demand_i


            # Update agents' tables and check convergence a la Johnson et al. 2021
            old_optimal_actions = [
                np.argmax(agents[i].q[:, old_states[i]]) for i in range(2)]
            for i in range(2):
                agents[i].transition(rewards[i], step)
            agent1.my_action_hist.append(agent1.a)
            agent1.opp_action_hist.append(agent2.a)
            agent2.my_action_hist.append(agent2.a)
            agent2.opp_action_hist.append(agent1.a)
            
            has_converged = agent1.check_if_converged(old_optimal_actions, step)

            if has_converged:
                break

        # Generate equilibrium price trajectory
        prices = []

        for _ in range(10):
            for i, agent in enumerate(agents):
                agent.choose_next_move(step = step)
                actions[i] = agent.a
            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            prices.append(agent1.action_price_space.take(actions))

        x = range(len(prices))
        y1 = [price[0] for price in prices]
        y2 = [price[1] for price in prices]

        if not self.shock:
            fig, ax = plt.subplots()
            ax.plot(x, y1, 'o-', label='price_1')
            ax.plot(x, y2, 'o-', label='price_2')
            ax.axhline(y=self.nash_prices[0], color='red', linestyle='--', label='Nash price 1')
            ax.axhline(y=self.nash_prices[1], color='green', linestyle='--', label='Nash price 2')
            ax.legend()
            plt.title("Equilibrium price trajectory")
            plt.show()
        

        # Capture prices before deviation
        prices_before_deviation = prices[-5:]  # last 5 periods before deviation
        
        # Test punishment if both agents deviate to the maximum price
        if self.shock:
            max_price_action = self.num_tot_actions - 1
            actions = [max_price_action, max_price_action]
            agent1.my_action_hist[-1] = actions[0]
            agent2.my_action_hist[-1] = actions[1]
            agent1.opp_action_hist[-1] = actions[1]
            agent2.opp_action_hist[-1] = actions[0]
            prices_after_deviation = []

            for _ in range(10):
                prices_after_deviation.append(agent1.action_price_space.take(actions))
                for i, agent in enumerate(agents):
                    agent.choose_next_move(step)
                    actions[i] = agent.a
                agent1.my_action_hist.append(actions[0])
                agent1.opp_action_hist.append(actions[1])
                agent2.my_action_hist.append(actions[1])
                agent2.opp_action_hist.append(actions[0])

            # Concatenate prices before and after deviation
            combined_prices = prices_before_deviation + prices_after_deviation

            x = range(len(combined_prices))
            y1 = [price[0] for price in combined_prices]
            y2 = [price[1] for price in combined_prices]

            fig, ax = plt.subplots()
            ax.plot(x, y1, 'o-', label='price_1')
            ax.plot(x, y2, 'o-', label='price_2')
            ax.axhline(y=self.nash_prices[0], color='red', linestyle='--', label='Nash price 1')
            ax.axhline(y=self.nash_prices[1], color='green', linestyle='--', label='Nash price 2')
            ax.legend()
            plt.title("Prices Before and After Deviation")
            plt.show()

class HotellingCollusionLearner():
    def __init__(self, num_possible_actions, num_possible_states, nash_prices, **kwargs):
        grid_lower_bound = kwargs.get('grid_lower_bound', min(nash_prices) - 0.5)  # default min price is min Nash - 0.1
        grid_upper_bound = kwargs.get('grid_upper_bound', max(nash_prices) + 0.5)  # default max price is max Nash + 1
        self.num_actions  = num_possible_actions  # number of discrete prices (seller's action space)
        self.num_states = num_possible_states

        self.learning_rate = kwargs.get('learning_rate', 0.15)
        self.discount_factor = kwargs.get('discount_factor', 0.95)
        self.beta = kwargs.get('beta', 0.00001)
        self.eps = []
        self.q = np.zeros((num_possible_actions, num_possible_states))
        self.action_price_space = np.linspace(
            grid_lower_bound, grid_upper_bound, self.num_actions)  # price grid
        self.a_i = kwargs.get('a_i', 2)  # product quality index for agent i
        self.c_i = kwargs.get('c_i', 0)  # seller cost for agent i
        self.a_j = kwargs.get('a_j', 2)  # product quality index for agent j
        self.c_j = kwargs.get('c_j', 0)  # seller cost for agent j
        self.theta = kwargs.get('theta', 1)  # Hotelling parameter
        self.max_steps = kwargs.get('max_steps', 1000000)  # control how long simulation takes to run
        
        self.init_q()
        self.my_action_hist = []
        self.opp_action_hist = []
    
    def determine_state(self):
        """Generates a state representation from your agent's and your opponent's action histories."""
        if len(self.my_action_hist) == 0 or len(self.opp_action_hist) == 0:
            return 0
        last_my_action = self.my_action_hist[-1]
        last_opp_action = self.opp_action_hist[-1]
        state = last_my_action * self.num_actions + last_opp_action
        return state
        
    def check_if_converged(self, old_optimal_actions, step):
        """Checks if Q matrices have converged, i.e., if optimal actions do not change for 100000 steps"""
        observation = self.determine_state()
        new_optimal_actions = [np.argmax(self.q[:, observation])]
        action_diff = np.sum(np.absolute(
            np.array(new_optimal_actions) - np.array(old_optimal_actions)))
        q_table_stable = True if action_diff == 0 else False

        has_converged = False
        if step == 1:
            self.convergence_counter = 0
        if q_table_stable:
            self.convergence_counter += 1
        else:
            self.convergence_counter = 0
        if self.convergence_counter == 100000:
            print("Converged: True")
            has_converged = True
            print("Convergence_counter:", self.convergence_counter)
            print("Done: ", has_converged)
            print("-------------------------\n\n\n")

        return has_converged

    def hotelling_demand_func(self, price_i, price_j): 
        demand_i = 0.5 + (self.a_i - price_i - self.a_j + price_j) / (2 * self.theta)
        return demand_i


    def init_q(self):
        """Used to initialize Q tables"""
        for s in range(self.num_states): 
            for a1 in range(self.num_actions): 
                reward = 0
                for a2 in range(self.num_actions):
                    price_i = self.action_price_space[a1]
                    price_j = self.action_price_space[a2]
                    demand_0 = self.hotelling_demand_func(price_i, price_j)
                    profit_0 = (price_i - self.c_i) * demand_0
                    # Assume all actions by the other agent are uniformly possible
                    reward += profit_0 / self.num_actions
                self.q[a1][s] = float(reward / (1 - self.discount_factor))


    def choose_next_move(self, step=0):
        state = self.determine_state()
        epsilon = np.exp(-1 * self.beta * step)
        self.eps.append(epsilon)
        if random.uniform(0, 1) < epsilon:
            price = random.randint(0, self.num_actions - 1)
        else:
            price = np.argmax(self.q[:, state])
        self.a = price

    def update_rule(self, reward):
        self.q[self.a][self.s] += self.learning_rate * \
            (reward + self.discount_factor *
             np.max(self.q[:, self.s_prime]) - self.q[self.a][self.s])

    def transition(self, my_reward, step):
        self.s_prime = self.determine_state()
        self.update_rule(my_reward)
        self.choose_next_move(step)
        self.s = self.s_prime

class LogitCollusionEnv():
    def __init__(self, agents, num_tot_actions, num_tot_states, nash_prices, seed=456, **kwargs) -> None:
        self.agents = agents 
        self.num_tot_actions = num_tot_actions
        self.num_tot_states = num_tot_states
        self.max_steps = kwargs.get('max_steps', 1000000)
        random.seed(seed)
        np.random.seed(seed)
        self.shock = kwargs.get('shock', False)
        self.nash_prices = nash_prices
    
    def run(self): 
        # We generate random prices to provide initial observation to Q learners
        num_tot_actions = self.num_tot_actions
        agents = self.agents
        agent1, agent2 = agents
        random_actions = [random.randint(0, num_tot_actions - 1), random.randint(0, num_tot_actions - 1)]
        agent1.my_action_hist.append(random_actions[0])
        agent1.opp_action_hist.append(random_actions[1])
        agent1.s = agent1.determine_state()
        agent1.choose_next_move(step = 0)
        
        agent2.my_action_hist.append(random_actions[1])
        agent2.opp_action_hist.append(random_actions[0])
        agent2.s = agent2.determine_state()
        agent2.choose_next_move(step = 0)

        actions = np.array([agent1.a, agent2.a])

        step = 0
        while step < self.max_steps:
            # Increment and print step count every 100000 steps
            step += 1
            if step % 100000 == 0:
                print("Steps completed: ", step)

            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            old_states = [agent1.determine_state(), agent2.determine_state()]
            for i, agent in enumerate(agents):
                agent.choose_next_move(step = step)
                actions[i] = agent.a

            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            
            prices = agent1.action_price_space.take(
                actions)  # Convert actions into prices

            # Compute rewards at current prices
            rewards = {}
            for i, agent in enumerate(agents):
                demand_i = np.exp((agent.a_i - prices[i]) / agent.mu) / (
                    np.sum(np.exp((agent.a_i - prices) / agent.mu)) + np.exp(agent.a_0 / agent.mu))
                rewards[i] = (prices[i] - agent.c_i) * demand_i

            # Update agents' tables and check convergence a la Johnson et al. 2021
            old_optimal_actions = [
                np.argmax(agents[i].q[:, old_states[i]]) for i in range(2)]
            for i in range(2):
                agents[i].transition(rewards[i], step)
            agent1.my_action_hist.append(agent1.a)
            agent1.opp_action_hist.append(agent2.a)
            agent2.my_action_hist.append(agent2.a)
            agent2.opp_action_hist.append(agent1.a)
            
            has_converged = agent1.check_if_converged(old_optimal_actions, step)

            if has_converged:
                break

        # Generate equilibrium price trajectory
        prices = []

        for _ in range(10):
            for i, agent in enumerate(agents):
                agent.choose_next_move(step = step)
                actions[i] = agent.a
            agent1.my_action_hist.append(actions[0])
            agent1.opp_action_hist.append(actions[1])
            agent2.my_action_hist.append(actions[1])
            agent2.opp_action_hist.append(actions[0])
            prices.append(agent1.action_price_space.take(actions))

        x = range(len(prices))
        y1 = [price[0] for price in prices]
        y2 = [price[1] for price in prices]

        if not self.shock:
            fig, ax = plt.subplots()
            ax.plot(x, y1, 'o-', label='price_1')
            ax.plot(x, y2, 'o-', label='price_2')
            ax.axhline(y=self.nash_prices[0], color='red', linestyle='--', label='Nash price 1')
            ax.axhline(y=self.nash_prices[1], color='green', linestyle='--', label='Nash price 2')
            ax.legend()
            plt.title("Equilibrium price trajectory")
            plt.show()
        

        # Capture prices before deviation
        prices_before_deviation = prices[-5:]  # last 5 periods before deviation
        
        # Test punishment if both agents deviate to the maximum price
        if self.shock:
            max_price_action = self.num_tot_actions - 1
            actions = [max_price_action, max_price_action]
            agent1.my_action_hist[-1] = actions[0]
            agent2.my_action_hist[-1] = actions[1]
            agent1.opp_action_hist[-1] = actions[1]
            agent2.opp_action_hist[-1] = actions[0]
            prices_after_deviation = []

            for _ in range(10):
                prices_after_deviation.append(agent1.action_price_space.take(actions))
                for i, agent in enumerate(agents):
                    agent.choose_next_move(step)
                    actions[i] = agent.a
                agent1.my_action_hist.append(actions[0])
                agent1.opp_action_hist.append(actions[1])
                agent2.my_action_hist.append(actions[1])
                agent2.opp_action_hist.append(actions[0])

            # Concatenate prices before and after deviation
            combined_prices = prices_before_deviation + prices_after_deviation

            x = range(len(combined_prices))
            y1 = [price[0] for price in combined_prices]
            y2 = [price[1] for price in combined_prices]

            fig, ax = plt.subplots()
            ax.plot(x, y1, 'o-', label='price_1')
            ax.plot(x, y2, 'o-', label='price_2')
            ax.axhline(y=self.nash_prices[0], color='red', linestyle='--', label='Nash price 1')
            ax.axhline(y=self.nash_prices[1], color='green', linestyle='--', label='Nash price 2')
            ax.legend()
            plt.title("Prices Before and After Deviation")
            plt.show()
        

class LogitCollusionLearner():
    def __init__(self, num_possible_actions, num_possible_states, nash_prices, **kwargs):
        grid_lower_bound = kwargs.get('grid_lower_bound', min(nash_prices) - 0.5)  # default min price is min Nash - 0.1
        grid_upper_bound = kwargs.get('grid_upper_bound', max(nash_prices) + 0.5)  # default max price is max Nash + 1
        self.num_actions  = num_possible_actions  # number of discrete prices (seller's action space)
        self.num_states = num_possible_states

        self.learning_rate = kwargs.get('learning_rate', 0.15)
        self.discount_factor = kwargs.get('discount_factor', 0.95)
        self.beta = kwargs.get('beta', 0.00001)
        self.eps = []
        self.q = np.zeros((num_possible_actions, num_possible_states))
        self.action_price_space = np.linspace(
            grid_lower_bound, grid_upper_bound, self.num_actions)  # price grid
        self.a_i = kwargs.get('a_i', 2)  # product quality index (assumed to be equal for all sellers)
        self.c_i = kwargs.get('c_i', 1)  # seller cost (assumed to be equal for all sellers)
        self.a_0 = kwargs.get('a_0', 0)  # quality of outside option
        self.mu = kwargs.get('mu', 0.25)  # horizontal differentiation parameter
        self.max_steps = kwargs.get('max_steps', 1000000)  # control how long simulation takes to run
        
        self.init_q()
        self.my_action_hist = []
        self.opp_action_hist = []

    
    def determine_state(self):
        """Generates a state representation from your agent's and your opponent's action histories."""
        if len(self.my_action_hist) == 0 or len(self.opp_action_hist) == 0:
            return 0
        last_my_action = self.my_action_hist[-1]
        last_opp_action = self.opp_action_hist[-1]
        state = last_my_action * self.num_actions + last_opp_action
        return state
        
    def check_if_converged(self, old_optimal_actions, step):
        """Checks if Q matrices have converged, i.e., if optimal actions do not change for 100000 steps"""
        observation = self.determine_state()
        new_optimal_actions = [np.argmax(self.q[:, observation])]
        action_diff = np.sum(np.absolute(
            np.array(new_optimal_actions) - np.array(old_optimal_actions)))
        q_table_stable = True if action_diff == 0 else False

        has_converged = False
        if step == 1:
            self.convergence_counter = 0
        if q_table_stable:
            self.convergence_counter += 1
        else:
            self.convergence_counter = 0
        if self.convergence_counter == 100000:
            print("Converged: True")
            has_converged = True
            print("Convergence_counter:", self.convergence_counter)
            print("Done: ", has_converged)
            print("-------------------------\n\n\n")

        return has_converged

    def logit_demand_func(self, price_i, price_j): 
        a_i = self.a_i  # Product quality index
        a_0 = self.a_0  # Quality of outside option
        mu = self.mu  # Horizontal differentiation parameter
        price_i = price_i  # Your price
        prices = np.array([price_i, price_j])  # Array of prices (i -> your price), (j -> opp price)
        
        demand_i = np.exp((a_i - price_i) / mu) / (np.sum(np.exp((self.a_i - prices) / mu)) + np.exp(a_0 / mu))
        return demand_i

    def init_q(self):
        """Used to initialize Q tables"""
        for s in range(self.num_states): 
            for a1 in range(self.num_actions): 
                reward = 0
                for a2 in range(self.num_actions):
                    price_i = self.action_price_space[a1]
                    price_j = self.action_price_space[a2]
                    demand_0 = self.logit_demand_func(price_i, price_j)
                    profit_0 = (price_i - self.c_i) * demand_0
                    # Assume all actions by the other agent are uniformly possible
                    reward += profit_0 / self.num_actions
                self.q[a1][s] = float(reward / (1 - self.discount_factor))


    def choose_next_move(self, step=0):
        state = self.determine_state()
        epsilon = np.exp(-1 * self.beta * step)
        self.eps.append(epsilon)
        if random.uniform(0, 1) < epsilon:
            price = random.randint(0, self.num_actions - 1)
        else:
            price = np.argmax(self.q[:, state])
        self.a = price

    def update_rule(self, reward):
        self.q[self.a][self.s] += self.learning_rate * \
            (reward + self.discount_factor *
             np.max(self.q[:, self.s_prime]) - self.q[self.a][self.s])

    def transition(self, my_reward, step):
        self.s_prime = self.determine_state()
        self.update_rule(my_reward)
        self.choose_next_move(step)
        self.s = self.s_prime


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
