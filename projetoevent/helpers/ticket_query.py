from projetoevent.models import Event, Ticket, TicketLog
from projetoevent.consts.action import ALREADY_CHECKED, INVALID, VALID
from django.db.models import Q


def get_ticket_data(event_id=None, gate_id=None, user=None, ticket=None):
    # if(event_id):
    valid_tickets = TicketLog.objects.filter(action=VALID).filter(
        event_id=event_id).order_by('id')[:10]
    invalid_tickets = TicketLog.objects.exclude(
        action=VALID).filter(
        event_id=event_id).order_by('created_at')[:10]
    valid_count = TicketLog.objects.filter(action=VALID).filter(
        event_id=event_id).count()
    invalid_count = TicketLog.objects.filter(action=INVALID).filter(
        event_id=event_id).count()
    already_checked_count = TicketLog.objects.filter(
        action=ALREADY_CHECKED).filter(
        event_id=event_id).count()
    total_count = Ticket.objects.filter(event__is_running=1).filter(
        conditional_ticket_filter(ticket)).filter(conditional_gate_filter(gate_id)).filter(
        event_id=event_id).count()

    # else:
    #     events = Event.objects.all().order_by('id')
    #     valid_tickets = TicketLog.objects.filter(
    #         action=VALID).order_by('id')[:10]
    #     invalid_tickets = TicketLog.objects.exclude(
    #         action=VALID).order_by('created_at')[:10]
    #     valid_count = TicketLog.objects.filter(action=VALID).count()
    #     invalid_count = TicketLog.objects.filter(action=INVALID).count()
    #     already_checked_count = TicketLog.objects.filter(
    #         action=ALREADY_CHECKED).count()
    #     total_count = Ticket.objects.filter(event__is_running=1).count(),
    #     gates = Ticket.objects.filter(event__is_running=1).distinct().order_by(
    #         'gate').values_list('gate', flat=True)

    events = Event.objects.all().order_by('id')
    gates = Ticket.objects.filter(event__is_running=1).distinct().order_by(
        'gate').values_list('gate', flat=True)

    # is uploading event
    is_uploading = Event.objects.filter(is_uploading=1).count()

    if(gate_id is not None and gate_id != ''):
        gate_id = int(gate_id)

    if(user is None):
        user = ''

    if(ticket is None):
        ticket = ''

    if(is_uploading is not None and is_uploading != '' and is_uploading > 0):
        is_uploading = True

    return {
        'events': events,
        'valid_tickets': valid_tickets,
        'invalid_tickets': invalid_tickets,
        'valid_count': valid_count,
        'invalid_count': invalid_count,
        'already_checked_count': already_checked_count,
        'total_count': total_count,
        'gates': gates,
        'event_id': int(event_id),
        'gate_id': gate_id,
        'user': user,
        'ticket': ticket,
        'is_uploading': is_uploading
    }


def format_event_to_json(event_dict):
    return {
        'valid_count': event_dict['valid_count'],
        'invalid_count': event_dict['invalid_count'],
        'already_checked_count': event_dict['already_checked_count'],
        'total_count': event_dict['total_count'],
        'valid_tickets': list(event_dict['valid_tickets'].values()),
        'invalid_tickets': list(event_dict['invalid_tickets'].values()),
        'event_id': int(event_dict['event_id'])
    }


def conditional_ticket_filter(ticket):
    if ticket != None and ticket != '':
        return Q(code=ticket)
    else:
        return Q()


def conditional_gate_filter(gate_id):
    if gate_id != None and gate_id != '':
        return Q(gate=gate_id)
    else:
        return Q()
