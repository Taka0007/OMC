Program OMC105
    Implicit None
    
    REAL :: ans
    INTEGER :: N
    
    ans = 1
    
    CONTINUE_LOOP: DO
        ans = ans + 1
        
        N = INT(ans)
        
        IF (ABS(f(N) - 100) <= 0.1) THEN
            EXIT CONTINUE_LOOP
        END IF
    END DO CONTINUE_LOOP
    
    WRITE(*,*) '解答:', ans
    WRITE(*,*) 'その時のf(n):', f(N)
    
CONTAINS
    
    FUNCTION f(N)
        IMPLICIT NONE
        INTEGER, INTENT(IN) :: N
        REAL :: f
        
        f = REAL(N) - (INT(SQRT(REAL(N))))**2
        
        RETURN
    END FUNCTION f

END Program OMC105
