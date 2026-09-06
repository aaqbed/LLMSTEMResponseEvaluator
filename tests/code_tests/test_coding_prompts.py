import pytest
import time
import threading



#P1: reverse_words

def test_p1_standard_cases(reverse_words):
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("Hello world") == "world Hello"
    assert reverse_words("I AM SO BORED!") == "BORED! SO AM I"

def test_p1_whitespace_preservation(reverse_words):
    assert reverse_words("  hello world  ") == "  world hello  "
    assert reverse_words("a   b  c") == "c   b  a"
    assert reverse_words("   ilove coding") == "   coding ilove"

def test_p1_edge_cases(reverse_words):
    assert reverse_words("") == ""
    assert reverse_words("single") == "single"
    assert reverse_words("  ") == "  "



#P2: first_unique_char

def test_p2_standard_cases(first_unique_char):
    assert first_unique_char("helloworld") == 0
    assert first_unique_char("helloworldhellosun") == 5

def test_p2_no_unique_char(first_unique_char):
    assert first_unique_char("aabb") == -1
    assert first_unique_char("cc") == -1

def test_p2_single_and_last_char(first_unique_char):
    assert first_unique_char("z") == 0
    assert first_unique_char("aabbc") == 4



#P3: search_rotated_array

def test_p3_found_elements(search_rotated_array):
    assert search_rotated_array([4,5,6,7,0,1,2], 0) == 4
    assert search_rotated_array([4,5,67,0,1,2], 5) == 1
    assert search_rotated_array([3,1],1) == 1
    assert search_rotated_array([1],1) == 0

def test_p3_missing_elements(search_rotated_array):
    assert search_rotated_array([4,5,6,7,0,1,2],3) == -1
    assert search_rotated_array([1],2) == -1
    assert search_rotated_array([],100) == -1



#P4: min_cost_tickets

def test_p4_standard_costs_1_7_30(min_cost_tickets):
    # Costs: 1-day = 1, 7-day = 7, 30-day = 30
    assert min_cost_tickets([1,4,6,7], [1,7,30]) == 4
    assert min_cost_tickets([1,4,6,7,8,20], [1,7,30]) == 6

def test_p4_standard_costs_2_7_15(min_cost_tickets):
    # Costs: 1-day = 2, 7-day = 7, 30-day = 15
    assert min_cost_tickets([1,4,6,7,8,20], [2,7,15]) == 11
    assert min_cost_tickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17

def test_p4_heavy_multi_day_discount(min_cost_tickets):
    # 7-day and 30-day passes are unusually cheap
    assert min_cost_tickets([1,2,3,4,5], [3,4,10]) == 4
    assert min_cost_tickets([1,5,10,15,20,25,30], [2,5,8]) == 8

def test_p4_very_expensive_multi_day_passes(min_cost_tickets):
    # Multi-day passes are expensive, forcing 1-day passes
    assert min_cost_tickets([1,3,5,7], [2,20,50]) == 8
    assert min_cost_tickets([1,2,4,7,15,28], [4,25,60]) == 24



#P5: BoundedBlockingQueue

def test_p5_fifo_and_size(BoundedBlockingQueue):
    q = BoundedBlockingQueue(3)
    assert q.size() == 0
    q.enqueue(10)
    q.enqueue(20)
    assert q.size() == 2
    assert q.dequeue() = 10
    assert q.size() == 1
    assert d.dequeue() == 20
    assert q.size() == 0

def test_p5_blocking_dequeue(BoundedBlockingQueue):
    q = BoundedBlockingQueue(2)
    dequeued = []

    def consumer():
        dequeued.append(q.dequeue())

    t = threading.Thread(target=consumer)
    t.start()
    time.sleep(0.05)

    assert len(dequeued) == 0
    q.enqueue(99)
    t.join(timeout=1.0)
    assert dequeued == [99]

def test_p5_blocking_enqueue(BoundedBlockingQueue):
    q = BoundedBlockingQueue(1)
    enqueued = []

    q.enqueue(1)

    def producer():
        q.enqueue(2)
        enqueued.append(True)

    t = threading.Thread(target=producer)
    t.start()
    time.sleep(0.05)

    assert len(enqueued) == 0
    assert q.dequeue() == 1
    t.join(timeout=1.0)
    assert len(enqueued) == 1
    assert q.dequeue() == 2