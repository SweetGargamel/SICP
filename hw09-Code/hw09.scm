;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (define (helper total biggest)
    (cond
      ((= total 0) (list '()))
      ((< total 0) '())
      ((<= biggest 0) '())
      (else
        (append
          (map (lambda (lst) (cons biggest lst))
               (helper (- total biggest) biggest))
          (helper total (- biggest 1))))))

  (helper total biggest))

(define (find n lst)
  (define (helper n lst index)
    (cond
      ((= n (car lst)) index )
      (else (helper n (cdr lst) (+ 1 index)))
      )
    )
  (helper n lst 0)
  )

(define (find-nest n sym)
  (define (helper n lst)
    (cond
      ((null? lst) #f)
      ((not (pair? lst)) (= n lst))
      (else 
      (or (helper n (car lst)) (helper n (cdr lst))
      ))))

  (cond
    ((number? (eval sym)) sym) 
    ((helper n (car (eval sym))) (find-nest n `(car ,sym))) 
    (else (find-nest n `(cdr ,sym))) 
  )
)



(define-macro (my/or operands)
  (cond
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)  ))
         (if t
           t
           (my/or ,(cdr operands))
           )))))

  
(define (replace-args args vals indices)
  (define (helper args vals indices result)
    (cond
      ((null? args) result)
      ((null? indices) (append result args))
      ((= (car indices) 0)
       (helper (cdr args) (cdr vals) (map (lambda (x) (- x 1)) (cdr indices)) (append result (list (car vals)))))
      (else
       (helper (cdr args) vals (map (lambda (x) (- x 1)) indices) (append result (list (car args)))))))
  (helper args vals indices '()))
(define (remaining-args args indices)
  (define (helper args indices result)
    (cond
      ((null? args) result)
      ((null? indices) (append result args))
      ((= (car indices) 0)
       (helper (cdr args) (map (lambda (x) (- x 1)) (cdr indices)) result))
      (else
       (helper (cdr args) (map (lambda (x) (- x 1)) indices) (append result (list (car args)))))))
  (helper args indices '()))

; (define-macro (k-curry fn args vals indices)
;   `(lambda ,(remaining-args args indices)   ;返回( a c)
;      (,fn ,@(replace-args args vals indices)))) ;返回( a 1 c 2)
    
(define-macro (k-curry fn args vals indices)
  `(lambda ,(remaining-args args indices)   ;返回( a c)
     ,(append `(,fn) (replace-args args vals indices)))) ;返回( a 1 c 2)

(define-macro (let* bindings expr)
  (if (null? bindings)
      `(let () ,expr)
      (let ((first-binding (car bindings))
            (rest-bindings (cdr bindings)))
        `(let (,(list (car first-binding) (cadr first-binding)))
           (let* ,rest-bindings ,expr)
           )
           )
           )
           )


;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)