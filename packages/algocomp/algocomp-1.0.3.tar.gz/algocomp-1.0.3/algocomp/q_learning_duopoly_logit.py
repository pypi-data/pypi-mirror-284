import numpy as np
import random
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    NUM_POSSIBLE_ACTIONS = 15
    
    # TODO: FILL OUT WITH NUMBER OF STATES IN YOUR STATE REPRESENTATION 
    NUM_POSSIBLE_STATES = NUM_POSSIBLE_ACTIONS**2
    ####################################################################

    # START SIMULATING THE GAME
    agent1 = LogitCollusionLearner(NUM_POSSIBLE_ACTIONS, NUM_POSSIBLE_STATES)
    agent2 = LogitCollusionLearner(NUM_POSSIBLE_ACTIONS, NUM_POSSIBLE_STATES)
    agents = [agent1, agent2]
    env = LogitCollusionEnv(agents, NUM_POSSIBLE_ACTIONS, NUM_POSSIBLE_STATES, nash_prices=[1.45, 1.95])
    env.run()
