from abc import ABC, abstractmethod
import threading
class DispenseChain(ABC):
    @abstractmethod
    def set_next_chain(self, next: 'DispenseChain'):
        pass
    @abstractmethod
    def can_dispense(self, amount):
        pass

    @abstractmethod
    def dispense(self, amount):
        pass


class NoteDispenser(DispenseChain):
    def __init__(self, note_val, note_cnt):
        self.note_val = note_val
        self.note_cnt = note_cnt
        self.next_chain = None
        self._lock = threading.Lock()

    def set_next_chain(self, chain: DispenseChain):
        self.next_chain = chain
    def can_dispense(self, amount):
        with self._lock:
            if amount < 0:
                return False
            if amount == 0:
                return True
            note_cnt = min(amount//self.note_val, self.note_cnt)
            rem_amt = amount - (note_cnt*self.note_val)
            if rem_amt==0:
                return True
            if self.next_chain:
                return self.next_chain.can_dispense(rem_amt)
            return False 
        
    def dispense(self, amount):
         with self._lock:
            if amount>= self.note_val:
                note_cnt = min(amount//self.note_val, self.note_cnt)
                rem_amt = amount - (note_cnt*self.note_val)

                if note_cnt > 0:
                    print(f"Dispensing {note_cnt} x {self.note_val} note(s)")
                    self.note_cnt = note_cnt
                
                if rem_amt > 0 and self.next_chain:
                    self.next_chain.dispense(rem_amt)
            else:
                self.next_chain.dispense(amount)


class NoteDispenser20(NoteDispenser):
    def __init__(self, note_cnt):
        super().__init__(20, note_cnt)

class NoteDispenser10(NoteDispenser):
    def __init__(self, note_cnt):
        super().__init__(10, note_cnt)

class NoteDispenser50(NoteDispenser):
    def __init__(self, note_cnt):
        super().__init__(50, note_cnt)