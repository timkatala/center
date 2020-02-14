from django.template.loader import render_to_string

from django.contrib import admin
from django.db.models import IntegerField, DateTimeField
from django.forms import TextInput, Textarea
from .utils import *
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from django.forms.models import BaseInlineFormSet, ModelForm
# from .forms import StudentForm
from django.db.models import Case,Sum, When, F, Value, Q
from django.http import HttpResponse, HttpResponseNotAllowed



class AlwaysChangedModelForm(ModelForm):
	def has_changed(self):
		return True


def p(t=None,s=None):


	class PaymentTabular(admin.TabularInline):
		model = Payment
		extra=0
		form = AlwaysChangedModelForm
		def get_queryset(self, request):
			qs = super(PaymentTabular, self).get_queryset(request)
			if t:
				qs=qs.filter(teacher=t.teacher)
			return qs
		if  t:
			verbose_name=t.teacher.name
			verbose_name_plural=t.teacher.name
		def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

			field = super(PaymentTabular, self).formfield_for_foreignkey(db_field, request, **kwargs)

			if db_field.name == 'teacher':
				if t:
					field.queryset = t.student.teacher.all()  
				# else:
				# 	field.queryset = s.teacher.all()
				
			if db_field.name == 'contract':
				if t:
					field.queryset = t.contracts.all()  
				if s:
					field.queryset = s.contracts.all()
			return field	
		def get_formset(self, request, obj=None, **kwargs):
			form = super(PaymentTabular, self).get_formset(request, obj, **kwargs)
			if t:
				form.form.base_fields['percent'].initial = t.percent
				form.form.base_fields['teacher'].initial = t.teacher

			return form	
	return PaymentTabular

class ContractTabular(admin.TabularInline):
	model = Contract
	extra=0


class StudentAdmin(admin.ModelAdmin):

	model = Student	
	inlines  = []
	
	list_editable = ('charachteristics',)
	
	list_display=('charachteristics','name','phone_number','fathers_phone','mothers_phone','shartnoma',)
	list_display_links=('name',)
	change_list_template='s.html'
	#form = StudentForm
	search_fields=['name',]
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':10,'width':10})},
		models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':10})},
	}
	def get_inline_instances(self ,request, obj):
		inlines = [p(None, obj), ContractTabular]
		#qs = Payment.objects.filter(student=obj).distinct('teacher')
		# for i in qs:
		# 	print(i)
		# 	inlines.append(p(i))

		self.inlines =inlines
		return super(StudentAdmin, self).get_inline_instances(request, obj)
	def shartnoma(self, obj):
		pays  = obj.contracts.all().annotate(
													debt=Sum(F('payments__has_to_pay')-F('payments__paid'))-Sum(Case(When(payments__period=timer(), then=F('payments__has_to_pay')-F('payments__paid')), output_field=IntegerField(), default=0)),
													#must_pay=Value(Case(When(payments__period=timer(), then=F('payments__has_to_pay')), output_field=IntegerField(), default=0)),
													#date=Case(When(payments__period=timer(), then='payments__date'), output_field=DateTimeField(), default=None)
													).order_by('teacher__name')
		d = []
		for t in pays:
			m = Payment.objects.get_or_create(contract=t, teacher=t.teacher, student=obj, period=timer())[0]
			d.append((m, t.debt+m.has_to_pay))
		s = render_to_string('r.html',{'pays':pays, 'd':d,
			})

		#print(d)
		# link = reverse("admin:auth_user_change", args=[1])
		#return format_html('<a href="{}">Edit {}</a>', link, obj.name)
		return format_html(s)
	shartnoma.allow_tags = True
	shartnoma.short_description = format_html(f"""Oldingi oylardan qarzi

															<th scope="col" class="column-loan">
													   <div class="text"><span>{MONTHS[datetime.datetime.now().month-1]} uchun<br>to’lashi kerak</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-paid">
													   <div class="text"><span>{MONTHS[datetime.datetime.now().month-1]}<br>uchun<br>to’ladi</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-paid">
													   <div class="text"><span>To’langansa’na
													</span></div>
													   <div class="clear"></div>
													   
													</th>
													""")
	def another(self, obj):
		# link = reverse("admin:auth_user_change", args=[1])
		#return format_html('<a href="{}">Edit {}</a>', link, obj.name)
		return format_html(f'<input type="text" name="param" value="{self.pays}" class="vTextField" maxlength="50" id="param">')
	shartnoma.allow_tags = True
	def changelist_view(self, request, extra_context=None):
		#print(request.POST)
		for i, v in request.POST.items():
			if i.startswith('params'):
				id = i.split('-')[1]
				Payment.objects.filter(pk=id).update(paid=v, has_to_pay=request.POST.get(f'topay-{id}'))
		return super(StudentAdmin, self).changelist_view(request, extra_context)
	def get_model_perms(self, request):
		if request.user.kassir:
			return HttpResponseNotAllowed
		return super(StudentAdmin, self).get_model_perms(request)
	def get_object(self, request, object_id, form_field=None):
		if request.user.kassir:
			return Htt
		return super().get_object(request, object_id, form_field=None)
	class Media:
		js = ('js/autoc.js','js/dfs.js','admin/js/inlines.js','admin/js/change_form.js','admin/js/prepopulate_init.js',)
# 		css={
# 		'all': ('css/jquery-ui.css',)
# }

	# def get_list_display(self, request):
	# 	extra_fields = [
	# 		f.name for model in self.inlines 
	# 		for f in model._meta.get_fields(include_hidden=False) 
	# 	]
	# 	return self.list_display + extra_fields

admin.site.register(Student,StudentAdmin)



class SalaryTabular(admin.TabularInline):
	model = Salary
	extra  =0


class TeacherAdmin(admin.ModelAdmin):

	model = Teacher	
	change_list_template='new.html'
	list_display=('name','shartnoma',)
	inlines=[SalaryTabular, p(None, None),]
	def shartnoma(self, obj):
		debt  = obj.salaries.all().aggregate(
													debt=Sum(-F('official')+F('paid'))-Sum(Case(When(period=timer(), then=-F('official')+F('paid')), 
														When(period=timer1(), then=-F('official')+F('paid')),output_field=IntegerField(), default=0)),
												
													)
		earned  = obj.payments.all().aggregate(
													
													previous=Sum((F('percent')*F('paid'))/100, filter=Q(period=timer1())),
												current=Sum((F('percent')*F('paid'))/100, filter=Q(period=timer())),
												debt=Sum((F('percent')*F('paid'))/100, filter=~(Q(period=timer())|Q(period=timer1()))),
											)
		#print(earned)
		previous, created = Salary.objects.get_or_create(period=timer1(), teacher=obj,
			defaults={'paid': 0, 'official':0})
		current, created = Salary.objects.get_or_create(period=timer(), teacher=obj,
			defaults={'paid': 0, 'official':0})
		if earned['debt']==None:
			earned['debt'] = 0
		d = {
		'id':obj.id,
			'debt':debt['debt']-earned['debt'],
			'earned':earned,
			'previous_debt':debt['debt']-earned['debt']-earned['previous']-previous.official+previous.paid,
			'current_debt':debt['debt']-earned['debt']-earned['previous']-previous.official+previous.paid-earned['current']-current.official+current.paid,
			'previous':previous,
			'current':current,
		}

		s = render_to_string('r1.html',d)
		#print(s)
		return format_html(s)
	shartnoma.allow_tags = True
	shartnoma.short_description = format_html(f"""Qarzi

															<th scope="col" class="column-previous-paid">
													   <div class="text"><span>Hisoblandi</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-previous-official">
													   <div class="text"><span>Rasmiy oylik</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-previous-earned">
													   <div class="text"><span>Naqd topdi
													</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-previous-debt">
													   <div class="text"><span>Qarzdorlik</span></div>
													   <div class="clear"></div>
													   
													</th>

															<th scope="col" class="column-current-paid">
													   <div class="text"><span>Hisoblandi</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-current-official">
													   <div class="text"><span>Rasmiy oylik</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-current-earned">
													   <div class="text"><span>Naqd topdi
													</span></div>
													   <div class="clear"></div>
													   
													</th>
													<th scope="col" class="column-current-debt">
													   <div class="text"><span>Qarzdorlik</span></div>
													   <div class="clear"></div>
													   
													</th>
													""")	
	def changelist_view(self, request, extra_context=None):
		#print(request.POST)
		for i, v in request.POST.items():
			if i.startswith('pr_paid'):
				id = i.split('-')[1]
				Salary.objects.filter(pk=id).update(paid=v, official=request.POST.get(f'pr_official-{id}'))
			if i.startswith('cur_paid'):
				id = i.split('-')[1]
				Salary.objects.filter(pk=id).update(paid=v, official=request.POST.get(f'cur_official-{id}'))
		return super(TeacherAdmin, self).changelist_view(request, extra_context)
	class Media:
		js = ('js/teacher.js',)
admin.site.register(Teacher, TeacherAdmin)



admin.site.register(Contract)

class PaymentAdmin(admin.ModelAdmin):

	model = Payment	
	save_as = True

	list_display=('teacher','period','paid', 'percent', )	
	list_editable=('period','paid','percent', )

	list_filter=('student','teacher',)	
	def get_queryset(self, request):
		if '_popup' in request.GET:
			request.GET = request.GET.copy()

			request.GET.pop('_popup')
			
		return  super(PaymentAdmin, self).get_queryset(request)

			
	# def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
	# 	context.update({
	# 	'show_save': True,
	# 	'show_save_and_continue': True,
	# 	'show_delete': True,
	# 	})
	# 	return super().render_change_form(request, context, add, change, form_url, obj)



admin.site.register(Payment, PaymentAdmin)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'last_name')
#     list_filter = ('is_staff', 'is_superuser')
#     def get_queryset(self, request):
#         return None

#     model  =User


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

