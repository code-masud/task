from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import ContentBlock, TermContent


@receiver(pre_save, sender=ContentBlock)
def delete_old_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return 

    try:
        old_file = ContentBlock.objects.get(pk=instance.pk).file
    except ContentBlock.DoesNotExist:
        return

    new_file = instance.file

    if old_file and old_file != new_file:
        old_file.delete(save=False)


@receiver(pre_save, sender=TermContent)
def delete_old_term_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_file = TermContent.objects.get(pk=instance.pk).file
    except TermContent.DoesNotExist:
        return

    new_file = instance.file

    if old_file and old_file != new_file:
        old_file.delete(save=False)


@receiver(post_delete, sender=ContentBlock)
def delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(save=False)


@receiver(post_delete, sender=TermContent)
def delete_term_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(save=False)