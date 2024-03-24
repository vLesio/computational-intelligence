
import time
from aipython.searchMPP import SearcherMPP
from aipython.stripsForwardPlanner import Forward_STRIPS
from aipython.stripsProblem import STRIPS_domain, Strips, Planning_problem

ITERATION_COUNT = 100

boolean = {False, True}
problem_domain = STRIPS_domain(
    {
        'RobLocation':{'coffee_shop', 'office', 'lab', 'mail_box'},
        'RobHasCoffee':boolean,
        'SamWantsCoffee':boolean,
        'SamHasUnreadLetter':boolean,
        'SamHasLetter':boolean,
        'RobHasLetter':boolean,
        'TelevisionIsOn':boolean,
        'RobHasRemote':boolean,
        'RobHasBatteries':boolean,
        'RemoteHasWorkingBatteries':boolean,
        'RobEnergy':boolean
    },
    {
        Strips(
            'mc_coffee_shop', 
            {'RobLocation':'coffee_shop'}, 
            {'RobLocation':'office'}),
        Strips(
            'mc_office', 
            {'RobLocation':'office'}, 
            {'RobLocation':'lab'}),
        Strips(
            'mc_lab', 
            {'RobLocation':'lab'}, 
            {'RobLocation':'mail_box'}),
        Strips(
            'mc_mail_box', 
            {'RobLocation':'mail_box'}, 
            {'RobLocation':'coffee_shop'}),
        Strips(
            'mcc_coffee_shop', 
            {'RobLocation':'coffee_shop'}, 
            {'RobLocation':'mail_box'}),
        Strips(
            'mcc_office', 
            {'RobLocation':'office'}, 
            {'RobLocation':'coffee_shop'}),
        Strips(
            'mcc_lab', 
            {'RobLocation':'lab'}, 
            {'RobLocation':'office'}),
        Strips(
            'mcc_mail_box', 
            {'RobLocation':'mail_box'}, 
            {'RobLocation':'lab'}),
        Strips(
            'get_coffee', 
            {
                'RobLocation':'coffee_shop', 
                'RobHasCoffee':False, 
                'RobEnergy': True
             }, 
            {'RobHasCoffee':True, 'RobEnergy': False}),
        Strips(
            'give_coffee_sam', 
            {'RobLocation':'office', 'RobHasCoffee':True}, 
            {'RobHasCoffee':False, 'SamWantsCoffee':False}),
        Strips(
            'get_mail', 
            {
                'RobLocation':'mail_box',
                'SamHasUnreadLetter':True, 
                'RobEnergy': True
             }, 
            {
                'RobHasLetter':True,
                'SamHasUnreadLetter':False, 
                'RobEnergy': False
             }),
        Strips(
            'give_mail_sam', 
            {'RobLocation':'office', 'RobHasLetter':True}, 
            {'RobHasLetter':False}),
        Strips(
            'turn_on_television', 
            {
                'RobLocation': 'office', 
                'RobHasRemote':True, 
                'RemoteHasWorkingBatteries': True, 
                'TelevisionIsOn':False
             }, 
            {'TelevisionIsOn':True}),
        Strips(
            'get_remote', 
            {
                'RobLocation': 'lab', 
                'RobHasRemote':False,
                'RobEnergy': True
                },
            {'RobHasRemote':True, 'RobEnergy': False}),
        Strips(
            'yeet_remote', 
            {'RobHasRemote': True, 'RobLocation': 'mail_box'},
            {'RobHasRemote': False}),
        Strips(
            'put_in_batteries', 
            {'RobHasBatteries':True, 'RobHasRemote': True},
            {'RobHasBatteries': False, 'RemoteHasWorkingBatteries': True}),
        Strips(
            'buy_batteries', 
            {'RobLocation':'coffee_shop'},
            {'RobHasBatteries': True}),
        Strips(
            'charge', 
            {'RobLocation':'lab', 'RobEnergy':False},
            {'RobEnergy': True})
    }
)

results = []

problem0 = Planning_problem( problem_domain,
    {
        'RobLocation':'lab',
        'SamHasUnreadLetter':True,
        'SamWantsCoffee':True,
        'RobHasCoffee':False,
        'RobHasLetter':False,
        'RobHasRemote':False,
        'TelevisionIsOn': False,
        'RobHasBatteries':False,
        'RemoteHasWorkingBatteries':False,
        'RobEnergy':True
    },
    {
        'RobLocation':'office'
    }
)


problem1 = Planning_problem( problem_domain,
    {
        'RobLocation':'lab',
        'SamHasUnreadLetter':True,
        'SamWantsCoffee':True,
        'RobHasCoffee':False,
        'RobHasLetter':False,
        'RobHasRemote':False,
        'TelevisionIsOn': False,
        'RobHasBatteries':False,
        'RemoteHasWorkingBatteries':False,
        'RobEnergy':True
    },
    {
        'SamWantsCoffee':False
    }
)

problem2 = Planning_problem( problem_domain,
    {
        'RobLocation':'lab',
        'SamHasUnreadLetter':True,
        'SamWantsCoffee':True,
        'RobHasCoffee':False,
        'RobHasLetter':False,
        'RobHasRemote':False,
        'TelevisionIsOn': False,
        'RobHasBatteries':False,
        'RemoteHasWorkingBatteries':False,
        'RobEnergy':True
    },
    {
        'SamWantsCoffee':False,
        'SamHasUnreadLetter':False,
        'RobHasLetter':False
    }
)

problem3 = Planning_problem( problem_domain,
    {
        'RobLocation':'coffee_shop',
        'SamHasUnreadLetter':True,
        'SamWantsCoffee':True,
        'RobHasCoffee':False,
        'RobHasLetter':False,
        'TelevisionIsOn': False,
        'RobHasRemote':False,
        'RobHasBatteries':False,
        'RemoteHasWorkingBatteries':False,
        'RobEnergy':True
    },
    {
        'SamWantsCoffee':False,
        'SamHasUnreadLetter':False,
        'RobHasLetter':False,
        'TelevisionIsOn': True,
        'RobHasRemote': False
    }
)

def SolveProblem(problem, problem_name:str, heuristic=None, iterations:int = 1):
    print(f'\033[33m[Runner] Solving problem: {problem_name}...\033[0m')
    start_time = time.time()
    
    for i in range(iterations):
        if heuristic is None:
            step = SearcherMPP(Forward_STRIPS(problem))
        else:
            step = SearcherMPP(Forward_STRIPS(problem, heuristic))
            
        step.search(should_print=(i == iterations-1)) # Only print the last iteration
        
    end_time = time.time()
    print(f'\033[32m[Runner] It took \033[34m{end_time-start_time}s\033[32m to find the solution in \033[34m{iterations} \033[32miterations. One iteration took on average \033[34m{(end_time-start_time)/iterations}s\033[0m\n')
    results.append((problem_name, (end_time-start_time), (end_time-start_time)/iterations))


dists = {
    'coffee_shop' : {
        'coffee_shop': 0,
        'office': 1,
        'lab': 2,
        'mail_box': 1,
        },
    'office' : {
        'office': 0,
        'lab': 1,
        'mail_box': 2,
        'coffee_shop': 1,
        },
    'lab' : {
        'lab': 0,
        'mail_box': 1,
        'coffee_shop': 2,
        'office': 1,
        },
    'mail_box' : {
        'mail_box': 0,
        'coffee_shop': 1,
        'office': 2,
        'lab': 1,
        },
}

def distance(current_location, goal_location):
    return dists[current_location][goal_location]


def heuristic_problem0(state, goal):
    return distance(state['RobLocation'],  goal['RobLocation'])


def heuristic_problem1(state, goal):
    if state['SamWantsCoffee'] == False:
        return 0
    if state['SamWantsCoffee'] == True and state['RobHasCoffee'] == False:
        return distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'office') + 1
    if state['RobHasCoffee'] == True:
        return distance(state['RobLocation'], 'office') + 1


def heuristic_problem2(state, goal):
    if state['SamHasUnreadLetter'] == True and state['SamWantsCoffee'] == False:
        return 0
    
    if state['RobHasLetter'] == False and state['RobHasCoffee'] == False:
        return min( 
            distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'coffee_shop') + 1 + distance('coffee_shop', 'office') ,
            distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'mail_box') + 1 + distance('mail_box', 'office') ,
        ) + 1
    
    if state['RobHasLetter'] == False:
        return distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'office') + 1
    
    if state['RobHasCoffee'] == False:
        return distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'office') + 1
    
    return distance(state['RobLocation'], 'office')


def heuristic_problem3(state, goal):
    if state['SamWantsCoffee'] == False and state['SamHasUnreadLetter'] == True and state['TelevisionIsOn'] == True:
        return 0
    
    if state['RobHasLetter'] == False and state['RobHasCoffee'] == False and state['RobHasRemote'] == False:
        return min(
            distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'coffee_shop') + 1 + distance('coffee_shop', 'lab') + 1 + distance('lab', 'office'),
            distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'lab') + 1 + distance('lab', 'coffee_shop') + 1 + distance('coffee_shop', 'office'), 
            distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'mail_box') + 1 + distance('mail_box', 'lab') + 1 + distance('lab', 'office'), 
            distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'lab') + 1 + distance('lab', 'mail_box') + 1 + distance('mail_box', 'office'), 
            distance(state['RobLocation'], 'lab') + 1 + distance('lab', 'coffee_shop') + 1 + distance('coffee_shop', 'mail_box') + 1 + distance('mail_box', 'office'),
            distance(state['RobLocation'], 'lab') + 1 + distance('lab', 'mail_box') + 1 + distance('mail_box', 'coffee_shop') + 1 + distance('coffee_shop', 'office'),
            ) + 1
    
    if state['RobHasLetter'] == False and state['RobHasCoffee'] == False:
        return min( 
            distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'coffee_shop') + 1 + distance('coffee_shop', 'office'), 
            distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'mail_box') + 1 + distance('mail_box', 'office')
            ) + 1
    
    if state['RobHasLetter'] == False and state['RobHasRemote'] == False:
        return min(
            distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'lab') + 1 + distance('lab', 'office'),
            distance(state['RobLocation'], 'lab') + 1 + distance('lab', 'mail_box') + 1 + distance('mail_box', 'office'),
            ) + 1
    
    if state['RobHasRemote'] == False and state['RobHasCoffee'] == False:
        return min( 
            distance(state['RobLocation'], 'lab') + 1 + distance('lab', 'coffee_shop') + 1 + distance('coffee_shop', 'office'),
            distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'lab') + 1 + distance('lab', 'office'),
            ) + 1
    
    if state['RobHasLetter'] == False:
        return distance(state['RobLocation'], 'mail_box') + 1 + distance('mail_box', 'office') + 1
    
    if state['RobHasCoffee'] == False:
        return distance(state['RobLocation'], 'coffee_shop') + 1 + distance('coffee_shop', 'office') + 1
    
    if state['RobHasRemote'] == False:
        return distance(state['RobLocation'], 'lab') + 1 + distance('lab', 'office') + 1
    
    return distance(state['RobLocation'], 'office') + 1


SolveProblem(problem0, 'Go to office [problem0]', iterations=ITERATION_COUNT)
SolveProblem(problem0, '[Heuristic] Go to office [problem0]', heuristic=heuristic_problem0, iterations=ITERATION_COUNT)

SolveProblem(problem1, 'Give Sam coffee [problem1]', iterations=ITERATION_COUNT)
SolveProblem(problem1, '[Heuristic] Give Sam coffee [problem1]', heuristic=heuristic_problem1, iterations=ITERATION_COUNT)

SolveProblem(problem2, 'Give Sam coffee and letter [problem2]', iterations=ITERATION_COUNT)
SolveProblem(problem2, '[Heuristic] Give Sam coffee and letter [problem2]', heuristic=heuristic_problem2, iterations=ITERATION_COUNT)

SolveProblem(problem3, 'Give Sam coffee, letter and turn on tv [problem3]', iterations=ITERATION_COUNT)
SolveProblem(problem3, '[Heuristic] Give Sam coffee, letter and turn on tv [problem3]',heuristic=heuristic_problem3, iterations=ITERATION_COUNT)


print('\033[32m[Runner] Results for all problems:\033[0m')
for i, result in enumerate(results):
    print(f'\033[33m[Runner] Problem: \033[31m{result[0]} \033[33mtook \033[34m{result[1]:.5f} \033[33m(\033[34m{result[2]:.5f}\033[33ms on average) to solve.\033[0m')
    if(i%2==1):
        if result[1] - results[i-1][1] > 0:
            print(f'\033[32mHeuristic time difference: \033[34m+{(result[1] - results[i-1][1]):.5f}, {(abs((result[1] - results[i-1][1]))*100/result[1]):.3f}\033[32m% slower\033[0m')
        else:
            print(f'\033[32mHeuristic time difference: \033[34m{(result[1] - results[i-1][1]):.5f}, {(abs((result[1] - results[i-1][1]))*100/result[1]):.3f}\033[32m% faster\033[0m')
        print('\n')
