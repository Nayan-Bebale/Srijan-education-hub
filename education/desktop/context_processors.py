def job_seeker(request):
    if request.user.is_authenticated:
        return {'job_seeker': request.user}
    else:
        return {}