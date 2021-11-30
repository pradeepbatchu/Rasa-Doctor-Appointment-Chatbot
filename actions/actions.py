from typing import Dict, Text, Any, List, Union, Optional
import logging
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk import Action, FormValidationAction

logger = logging.getLogger(__name__)

class ValidateEntitiesForm(Action):
    def name(self) -> Text:
        return "transact_search_form"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["book_type","PERSON","time2"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        book_type = tracker.get_slot("book_type")
        start_time = tracker.get_slot("time")
        time2 = tracker.get_slot("time2")
        #dispatcher.utter_message("date {}".format(start_time))
        if book_type == "book" or book_type == "test":
            print(book_type)
            dispatcher.utter_message(response="utter_name_time_confirm",)
        else:            
            dispatcher.utter_message(response="utter_name_confirm")
        return [SlotSet('book_type', None),SlotSet('time', None),SlotSet('time2', None),SlotSet('PERSON', None)]

