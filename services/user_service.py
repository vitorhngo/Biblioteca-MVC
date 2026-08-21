from utils import enums
import utils.exceptions as exc

from models.loan import Loan
from models.user import User

class UserService:
    def remove(self, user_id: int) -> enums.DeleteResult:
        user = User.find_by_id(user_id)
        if user is None:
            raise exc.UserNotFoundError()

        if Loan.all_active_for_user(user_id):
            user.deactivate()
            return enums.DeleteResult.DEACTIVATED

        user.delete()
        return enums.DeleteResult.DELETED