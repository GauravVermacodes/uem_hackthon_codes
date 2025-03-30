from django.shortcuts import render, redirect
from .form import LostItemForm, FoundItemForm
from .models import LostItem, FoundItem
from .google_vision import get_image_labels
from .twilio_sms import send_sms
from django.contrib import messages

def Homepage(request):
    messages.success(request, "Lost item reported successfully!")
    return render(request,"index.html")

def report_lost(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            lost_item = form.save()

            return redirect("Homepage")
    else:
        form = LostItemForm()
    return render(request, "report_lost.html", {"form": form})

def report_found(request):
    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            found_item = form.save()
            labels_found = get_image_labels(found_item.image.path)

            # Check for matches in database
            lost_items = LostItem.objects.all()
            for lost_item in lost_items:
                labels_lost = get_image_labels(lost_item.image.path)
                if any(label in labels_lost for label in labels_found):
                    send_sms(lost_item.contact_number, "We found a match for your lost item!")
                    send_sms(found_item.contact_number, "Your found item matches a lost item!")
                    break

            return redirect("Homepage")
    else:
        form = FoundItemForm()
    return render(request, "report_found.html", {"form": form})
