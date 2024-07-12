# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/3/19 18:18
# @Author  : heji
# @Email   : lc299034@antgroup.com
# @FileName: executing_agent.py
"""Executing Agent module."""
import copy
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from typing import Optional, Any

from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.plan.planner.planner import Planner
from agentuniverse.agent.plan.planner.planner_manager import PlannerManager


class ExecutingAgent(Agent):
    """Executing Agent class."""

    executor: Optional[Any] = ThreadPoolExecutor(max_workers=10, thread_name_prefix="executing_agent")

    def input_keys(self) -> list[str]:
        """Return the input keys of the Agent."""
        return ['planning_result']

    def output_keys(self) -> list[str]:
        """Return the output keys of the Agent."""
        return ['executing_result']

    def parse_input(self, input_object: InputObject, agent_input: dict) -> dict:
        """Agent parameter parsing.

        Args:
            input_object (InputObject): input parameters passed by the user.
            agent_input (dict): agent input preparsed by the agent.
        Returns:
            dict: agent input parsed from `input_object` by the user.
        """
        agent_input['input'] = input_object.get_data('input')
        agent_input['framework'] = input_object.get_data('planning_result').get_data('framework')
        self.agent_model.profile.setdefault('prompt_version', 'default_executing_agent.cn')
        return agent_input

    def parse_result(self, planner_result: dict) -> dict:
        """Planner result parser.

        Args:
            planner_result(dict): Planner result
        Returns:
            dict: Agent result object.
        """
        llm_result = []
        executing_result = []
        futures = planner_result.get('futures')
        for future in futures:
            task_result = future.result()
            llm_result.append(task_result)
            executing_result.append({
                'input': task_result['input'], 'output': task_result['output']
            })

        return {'executing_result': executing_result, 'llm_result': llm_result}

    def execute(self, input_object: InputObject, agent_input: dict) -> dict:
        """Execute agent instance.

        Args:
            input_object (InputObject): input parameters passed by the user.
            agent_input (dict): agent input parsed from `input_object` by the user.

        Returns:
            dict: Agent result object.
        """
        framework = agent_input.get('framework', [])
        futures = []
        for task in framework:
            # note: agent input shallow copy.
            agent_input_copy: dict = dict(agent_input)
            agent_input_copy['input'] = task
            planner: Planner = PlannerManager().get_instance_obj(self.agent_model.plan.get('planner').get('name'))
            futures.append(
                self.executor.submit(planner.invoke, self.agent_model, agent_input_copy,
                                     self.process_intput_object(input_object, task, planner.input_key)))
        wait(futures, return_when=ALL_COMPLETED)
        return {'futures': futures}

    def process_intput_object(self, input_object: InputObject, subtask: str, planner_input_key: str) -> InputObject:
        """Process input object for the executing agent.

        Args:
            input_object (InputObject): input parameters passed by the user.
            subtask (str): subtask to be executed.
            planner_input_key (str): planner input key.

        Returns:
            input_object (InputObject): processed input object.
        """
        # get agent toolsets.
        action: dict = self.agent_model.action or dict()
        tools: list = action.get('tool') or list()
        # note: input object shallow copy.
        input_object_copy: InputObject = InputObject(input_object.to_dict())
        # wrap input_object for agent knowledge.
        input_object_copy.add_data(planner_input_key, subtask)
        # wrap input_object for agent toolsets.
        for tool_name in tools:
            tool = ToolManager().get_instance_obj(tool_name)
            if tool is None:
                continue
            # note: only insert the first key of tool input.
            input_object_copy.add_data(tool.input_keys[0], subtask)
        return input_object_copy
