def bouncingBall(h, bounce, window):
    if( h > 0 and 0 < bounce < 1 and window < h) :
        new_height=h * bounce
        count= 1
        while(new_height>= window) : 
            count+=2
            new_height*=bounce
        return count
    else:
        return -1