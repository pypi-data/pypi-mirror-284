from fancykimai.functions.kimai import kimai_request
from fancykimai.functions.config import get_config
from iterfzf import iterfzf

def select_activity(ctx, param, value: str, debug=False, select_function=False) -> str:
    '''
    Select an activity from the list of activities in Kimai and return the id
    '''
    default = get_config('activity')
    if debug:
        print(f"Default activity: {default}")
    activities = kimai_request('api/activities')
    if debug:
        print(f"Activities: {activities}")
    if value:
        # Check if value is in the id or name of the activities
        for activity in activities:
            if value == activity['id']:
                if debug:
                    print(f"Found activity by id: {activity['id']}")
                return activity['id']
            if value == activity['name']:
                if debug:
                    print(f"Found activity by name: {activity['id']}")
                return activity['id']
        # If not found, return an error
        if debug:
            print(f"Activity not found")
        raise ValueError('Activity not found')
    else:
        if debug:
            print(f"No value given")
        # If no value is given, but there's a default activity, return the id
        # if it's a select function, don't return the default activity
        if default and not select_function:
            if debug:
                print(f"Returning default activity: {default}")
            return default
        # If no value is given and there's no default activity, prompt the user
        activity_names = [f"{activity['id']} - {activity['name']}" for activity in activities]
        selected_activity = iterfzf(activity_names)
        if debug:
            print(f"Selected activity: {selected_activity}")
        if selected_activity:
            if debug:
                print(f"Returning selected activity: {selected_activity.split(' - ')[0]}")
            return selected_activity.split(' - ')[0]
        else:
            raise ValueError('Activity not found')

