'''
Created on 30 avr. 2018

@author: PASTOR Robert
'''

import numpy
import math

''' % Compute system inputs and updated state.'''
''' % Note that input = [$\gamma_1$, $\ldots$, $\gamma_4$] '''
def pd_controller(state, thetadot):
    ''' % Controller gains, tuned by hand and intuition.'''
    Kd = 4;
    Kp = 3;

    ''' % Initialize the integral if necessary. '''
    if ~isfield(state, 'integral'):
        params.integral = numpy.zeros(3, 1);
    ''' end'''

    ''' % Compute total thrust '''
    total = state.m * state.g / state.k / (math.cos(state.integral(1)) * math.cos(state.integral(2)));

    ''' % Compute errors '''
    e = Kd * thetadot + Kp * params.integral;

    ''' % Solve for the inputs, $\gamma_i$ '''
    input = error2inputs(params, accels, total);
 
    ''' % Update the state '''
    params.integral = params.integral + params.dt .* thetadot;
    
    return [input, state]
''' end  '''

''' % Compute system inputs and updated state. '''
''' % Note that input = [$\gamma_1$, $\ldots$, $\gamma_4$] '''
def  pid_controller(state, thetadot):
    ''' % Controller gains, tuned by hand and intuition. '''
    Kd = 4;
    Kp = 3;
    Ki = 5.5;

    ''' % Initialize the integral if necessary. '''
    if ~isfield(state, 'integral'):
        params.integral = zeros(3, 1);
        params.integral2 = zeros(3, 1);
    ''' end '''

    '''% Prevent wind-up '''
    if max(abs(params.integral2)) > 0.01:
        params.integral2(:) = 0;
    '''end '''

    ''' % Compute total thrust '''
    total = state.m * state.g / state.k / (cos(state.integral(1)) * cos(state.integral(2)));

    ''' % Compute errors '''
    e = Kd * thetadot + Kp * params.integral - Ki * params.integral2;

    ''' % Solve for the inputs, $\gamma_i$ '''
    input = error2inputs(params, accels, total);

    ''' % Update the state '''
    params.integral = params.integral + params.dt .* thetadot;
    params.integral2 = params.integral2 + params.dt .* params.integral;
    
    return [input, state]

''' end '''


