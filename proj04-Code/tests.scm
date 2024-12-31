;;; Test cases for Scheme.
;;;
;;; In order to run only a prefix of these examples, add the line
;;;
;;; (exit)
;;;
;;; after the last test you wish to run.

;;; ********************************
;;; *** Add your own tests here! (Optional) ***
;;; ********************************

;;; These are examples from several sections of "The Structure
;;; and Interpretation of Computer Programs" by Abelson and Sussman.

;;; License: Creative Commons share alike with attribution
(define (factor n acc)
  (if (= n 0)
      acc
      (factor (- n 1) (* acc n))))

(factor 10 1)