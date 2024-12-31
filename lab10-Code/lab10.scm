;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s)
    nil
    (if (f (car s))
      (cons-stream (car s) (filter-stream f (cdr-stream s)))
      (filter-stream f (cdr-stream s)))))




(define (slice s start end)
  (define (helper s index start end)
    (cond
      [(null? s) nil]
      [(and (< index end ) (>= index start)) (cons (car s) (helper (cdr-stream s) (+ index 1) start end ) )]
      [(>= index end) nil]
      [else (helper (cdr-stream s) (+ index 1) start end )]
      )
    )
  (if (>= start end)
    nil
    (helper s 0 start end)
    )
  )

(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))




(define factorials
  (cons-stream 1 (combine-with * factorials (naturals 1))))


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))
  
; For this problem, you may use the naturals, combine-with, factorials defined above and built-in function expt.
; We highly recommend you do not define any other helper functions. Such problems are likely to appear on final exam.

; Write function exp, which returns a stream where the nth term represents the degree-n polynomial expansion for ex
; , which is ∑i=0nxii!
; .
x
  
  

(define (exp x)
  (define helper-stream (cons-stream x helper-stream))
  (cons-stream 1
    (combine-with + (exp x)
      (combine-with / (combine-with expt helper-stream (naturals 1))  (cdr-stream factorials)))
      )
    )


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (define (helper s lst former)
    (cond
      [(null? s) (cons-stream lst nil)]
      [(null? former) (helper (cdr-stream s) (append lst (cons (car s) nil) ) (car s)) ]
      [(< (car s) former) (cons-stream lst (helper s '() nil)) ]
      [else (helper (cdr-stream s) (append lst (cons (car s) nil) ) (car s))]
      )
    )
  (if (null? s)
    nil
    (helper s '() nil)
    )
  )


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
