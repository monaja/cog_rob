class MIMoStandupEnv(MIMoEnv):
    def __init__(self,
             model_path=STANDUP_XML,
             proprio_params=DEFAULT_PROPRIOCEPTION_PARAMS,
             touch_params=None,
             vision_params=None,
             vestibular_params=DEFAULT_VESTIBULAR_PARAMS,
             done_active=False,
             **kwargs,
             ):

        super().__init__(model_path=model_path,
                         proprio_params=proprio_params,
                         touch_params=touch_params,
                         vision_params=vision_params,
                         vestibular_params=vestibular_params,
                         done_active=done_active,
                         **kwargs,)

def get_achieved_goal(self):
    return self.data.body('head').xpos[2]

def is_success(self, achieved_goal, desired_goal):
    return False

def is_failure(self, achieved_goal, desired_goal):
    return False

def is_truncated(self):
    return False

def sample_goal(self):
    return 0.0

def compute_reward(self, achieved_goal, desired_goal, info):
    quad_ctrl_cost = 0.01 * np.square(self.data.ctrl).sum()
    reward = achieved_goal - 0.2 - quad_ctrl_cost
    return reward

def reset_model(self):
    self.set_state(self.init_qpos, self.init_qvel)
    qpos = self.init_crouch_position

    # set initial positions stochastically
    qpos[7:] = qpos[7:] + self.np_random.uniform(low=-0.01, high=0.01, size=len(qpos[7:]))

    # set initial velocities to zero
    qvel = np.zeros(self.data.qvel.ravel().shape)

    self.set_state(qpos, qvel)

    # perform 100 steps with no actions to stabilize initial position
    actions = np.zeros(self.action_space.shape)
    self._set_action(actions)
    mujoco.mj_step(self.model, self.data, nstep=100)

    return self._get_obs()
