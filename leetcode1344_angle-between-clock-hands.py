def angleClock(self, hour: int, minutes: int) -> float:
        
        
        hour = hour * 5.00
        
        ans = hour + (minutes*(2.50/30))
        ans = abs(ans - minutes)
        
        angle = ans * 6.00
        
        if angle <= 180.00:
            return angle
        else:
            return (360.00-angle)