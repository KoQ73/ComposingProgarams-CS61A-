(define (ascending? asc-lst)
    (if (null? asc-lst)
        #t
        (if (or (null? (cdr asc-lst)) (<= (car asc-lst) (car (cdr asc-lst))))
            (ascending? (cdr asc-lst))
            #f
        )
    )
)

(define (my-filter pred s)
    (if (null? s)
        nil
        (begin
            (define first (car s))
            (define rest (cdr s))
            (if (pred first)
                (cons first (my-filter pred rest))
                (my-filter pred rest)
            )
        )
    )
)

(define (interleave lst1 lst2)
    (cond
        ((and (null? lst1) (null? lst2)) nil)
        ((null? lst1)
            (cons (car lst2) (interleave nil (cdr lst2)))
        )
        ((null? lst2)
            (cons (car lst1) (interleave nil (cdr lst1)))
        )
        (else
            (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))
        )
    )
)

(define (no-repeats lst)
    (if (null? lst)
        nil
        (begin
            (define first (car lst))
            (define new (my-filter (lambda (x) (not (= first x))) lst))
            (cons first (no-repeats new))
        )
    )
)
