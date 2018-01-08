from decimal import Decimal

########################################################################
class Fees(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None

    # ----------------------------------------------------------------------
    @property
    def fee(self):
        """
        Return the current fee
        """
        return self._fee

    # ----------------------------------------------------------------------
    @fee.setter
    def fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

if __name__ == '__main__':
    f = Fees()
    f.fee = '222'
    print(f.fee)