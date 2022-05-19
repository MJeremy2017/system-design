from __future__ import annotations
from queue import Queue
from abc import ABC, abstractmethod
from typing import List


class CallOperation:
    def __init__(self):
        self.is_working = False

    def answer_call(self, operator: Operator, call: Call):
        if self.is_working:
            print("currently working ...")
            return False
        print(f"operator {operator.get_name()} is answering call from {call.user_id}")
        self.is_working = True
        return True


class Operator(ABC):
    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def answer_call(self, call: Call) -> bool:
        ...

    @abstractmethod
    def delegate(self, call: Call) -> bool:
        ...

    @abstractmethod
    def is_available(self) -> bool:
        ...


class Director(Operator):
    def __init__(self, name: str, call_ops: CallOperation):
        self.name = name
        self.call_ops = call_ops

    def get_name(self) -> str:
        return "director"

    def answer_call(self, call: Call) -> bool:
        return self.call_ops.answer_call(self, call)

    def delegate(self, call: Call) -> bool:
        return False

    def is_available(self) -> bool:
        return not self.call_ops.is_working


class Supervisor(Operator):
    def __init__(self, name: str, directors: List[Director], call_ops: CallOperation):
        self.name = name
        self.directors = directors
        self.call_ops = call_ops

    def get_name(self) -> str:
        return "supervisor"

    def answer_call(self, call: Call) -> bool:
        return self.call_ops.answer_call(self, call)

    def delegate(self, call: Call) -> bool:
        for drt in self.directors:
            if drt.is_available():
                return drt.answer_call(call)
        return False

    def is_available(self) -> bool:
        return not self.call_ops.is_working


class NormalOperator(Operator):
    def __init__(self, name: str, supervisors: List[Supervisor], call_ops: CallOperation):
        self.name = name
        self.supervisors = supervisors
        self.call_ops = call_ops

    def is_available(self) -> bool:
        return not self.call_ops.is_working

    def get_name(self) -> str:
        return "normal operator"

    def answer_call(self, call: Call) -> bool:
        return self.call_ops.answer_call(self, call)

    def delegate(self, call: Call) -> bool:
        for sup in self.supervisors:
            if sup.is_available():
                return sup.answer_call(call)
        return self.supervisors[0].delegate(call)


class Call:
    def __init__(self, number: str, user_id: str):
        self.number = number
        self.user_id = user_id


class CallCenter:
    def __init__(self, operators: List[Operator]):
        self.operators: List[Operator] = operators
        self.available_operators: Queue[Operator] = Queue()
        self.working_operators: Queue[Operator] = Queue()
        for op in self.operators:
            if op.is_available:
                self.available_operators.put(op)
            else:
                self.working_operators.put(op)
        self.call_queue: Queue[Call] = Queue()

    def answer_call(self, call: Call) -> bool:
        if self.available_operators.empty():
            op: Operator = self.working_operators.get()
            self.working_operators.put(op)
            if op.delegate(call):
                return True
            self.call_queue.put(call)
            print("All operators are busy, putting call into a call_queue")
            return False
        op: Operator = self.available_operators.get()
        self.working_operators.put(op)
        op.answer_call(call)
        return True

    def add_operator(self, operator: Operator):
        if operator.is_available:
            self.available_operators.put(operator)
        else:
            self.working_operators.put(operator)


if __name__ == '__main__':
    supervisor = Supervisor("sup_sup", [], CallOperation())
    operators = []
    for i in range(1):
        op = NormalOperator("op_" + str(i), [supervisor], CallOperation())
        operators.append(op)

    cc = CallCenter(operators)
    call = Call("12345", "user_1")
    cc.answer_call(call)
    call = Call("22345", "user_2")
    cc.answer_call(call)
