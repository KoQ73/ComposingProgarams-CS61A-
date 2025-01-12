(define (square n) (* n n))

(define (pow base exp)
  (cond
    ((= exp 1) base)
    ((even? exp)
      (let ((half-exp (pow base (/ exp 2))))
        (square half-exp)
      )
    )
    ((odd? exp)
      (* base (pow base (- exp 1)))
    )
  )
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)
