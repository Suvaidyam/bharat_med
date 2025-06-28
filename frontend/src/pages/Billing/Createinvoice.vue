<template>
	<div class="min-h-screen">
		<!-- Header -->
		<div class="bg-white">
			<div class="px-4 sm:px-6 lg:px-8 py-4">
				<div class="flex items-center justify-between">
					<div>
						<h1 class="text-2xl font-semibold text-gray-900">Create New Invoice</h1>
						<p class="text-sm text-gray-600">Enter the details for the new invoice.</p>
					</div>
					<div class="flex space-x-3">
						<button
							@click="saveAsDraft"
							class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
						>
							Save as Draft
						</button>
						<button
							@click="createInvoice"
							class="px-4 py-2 text-sm font-medium text-white bg-gray-900 border border-transparent rounded-md hover:bg-gray-800"
						>
							Create Invoice
						</button>
					</div>
				</div>
			</div>
		</div>

		<div class="px-4 sm:px-6 lg:px-8 py-6">
			<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
				<!-- Left Column - Invoice Details -->
				<div class="lg:col-span-2 space-y-6">
					<!-- Invoice Details Card -->
					<div class="bg-white shadow rounded-lg p-6">
						<h2 class="text-lg font-medium text-gray-900 mb-4">Invoice Details</h2>
						<p class="text-sm text-gray-600 mb-6">
							Enter the details for the new invoice.
						</p>

						<div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Invoice Number</label
								>
								<input
									v-model="invoice.number"
									type="text"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
									readonly
								/>
							</div>
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Invoice Date</label
								>
								<input
									v-model="invoice.date"
									type="date"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								/>
							</div>
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Due Date</label
								>
								<input
									v-model="invoice.dueDate"
									type="date"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								/>
							</div>
						</div>

						<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Invoice Type</label
								>
								<select
									v-model="invoice.type"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								>
									<option>Standard Invoice</option>
									<option>Recurring Invoice</option>
									<option>Credit Note</option>
								</select>
							</div>
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Reference / PO Number (Optional)</label
								>
								<input
									v-model="invoice.reference"
									type="text"
									placeholder="Enter reference or PO number"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								/>
							</div>
						</div>
					</div>

					<!-- Items & Services Card -->
					<div class="bg-white shadow rounded-lg p-6">
						<div class="flex items-center justify-between mb-4">
							<h2 class="text-lg font-medium text-gray-900">Items & Services</h2>
							<button
								@click="addItem"
								class="px-3 py-1 bg-gray-900 text-white text-sm rounded-md hover:bg-gray-800"
							>
								+ Add Item
							</button>
						</div>

						<div class="overflow-x-auto">
							<table class="w-full">
								<thead>
									<tr class="text-left text-sm font-medium text-gray-700">
										<th class="pb-3 w-8"></th>
										<th class="pb-3">Description</th>
										<th class="pb-3 w-20">Quantity</th>
										<th class="pb-3 w-24">Unit Price</th>
										<th class="pb-3 w-24">Total</th>
										<th class="pb-3 w-8"></th>
									</tr>
								</thead>
								<tbody class="space-y-2">
									<tr
										v-for="(item, index) in invoice.items"
										:key="index"
										class="border-t border-gray-200"
									>
										<td class="py-3">
											<input
												type="checkbox"
												v-model="item.selected"
												class="h-4 w-4 text-blue-600 border-gray-300 rounded"
											/>
										</td>
										<td class="py-3">
											<select
												v-model="item.description"
												class="w-full px-2 py-1 border border-gray-300 rounded text-sm focus:ring-blue-500 focus:border-blue-500"
											>
												<option value="">Select service or item</option>
												<option value="Blood Test - Basic Panel - $80.00">
													Blood Test - Basic Panel - $80.00
												</option>
												<option value="Consultation - General - $150.00">
													Consultation - General - $150.00
												</option>
												<option value="X-Ray - Chest - $120.00">
													X-Ray - Chest - $120.00
												</option>
											</select>
											<textarea
												v-model="item.additionalDescription"
												placeholder="Additional description"
												class="w-full px-2 py-1 mt-1 border border-gray-300 rounded text-sm resize-none"
												rows="1"
											></textarea>
										</td>
										<td class="py-3">
											<input
												v-model.number="item.quantity"
												type="number"
												min="1"
												class="w-full px-2 py-1 border border-gray-300 rounded text-sm text-center focus:ring-blue-500 focus:border-blue-500"
											/>
										</td>
										<td class="py-3">
											<input
												v-model.number="item.unitPrice"
												type="number"
												step="0.01"
												class="w-full px-2 py-1 border border-gray-300 rounded text-sm text-center focus:ring-blue-500 focus:border-blue-500"
											/>
										</td>
										<td class="py-3 text-center font-medium">
											${{ (item.quantity * item.unitPrice).toFixed(2) }}
										</td>
										<td class="py-3">
											<button
												@click="removeItem(index)"
												class="text-red-500 hover:text-red-700"
											>
												<svg
													class="w-4 h-4"
													fill="none"
													stroke="currentColor"
													viewBox="0 0 24 24"
												>
													<path
														stroke-linecap="round"
														stroke-linejoin="round"
														stroke-width="2"
														d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
													/>
												</svg>
											</button>
										</td>
									</tr>
								</tbody>
							</table>
						</div>

						<!-- Invoice Totals -->
						<div class="mt-6 bg-gray-50 p-4 rounded-lg">
							<div class="flex justify-end">
								<div class="w-64 space-y-2">
									<div class="flex justify-between text-sm">
										<span>Subtotal:</span>
										<span>${{ subtotal.toFixed(2) }}</span>
									</div>
									<div class="flex justify-between text-sm">
										<span>Tax (8%):</span>
										<span>${{ tax.toFixed(2) }}</span>
									</div>
									<div class="flex justify-between text-sm">
										<span>Discount:</span>
										<span>-${{ discount.toFixed(2) }}</span>
									</div>
									<div
										class="flex justify-between font-medium text-lg border-t pt-2"
									>
										<span>Total:</span>
										<span>${{ total.toFixed(2) }}</span>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- Additional Information Card -->
					<div class="bg-white shadow rounded-lg p-6">
						<h2 class="text-lg font-medium text-gray-900 mb-4">
							Additional Information
						</h2>

						<div class="space-y-4">
							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Notes</label
								>
								<textarea
									v-model="invoice.notes"
									placeholder="Enter any additional notes for this invoice"
									rows="4"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 resize-none"
								></textarea>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Payment Terms</label
								>
								<select
									v-model="invoice.paymentTerms"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								>
									<option>Net 30 Days</option>
									<option>Net 15 Days</option>
									<option>Net 60 Days</option>
									<option>Due on Receipt</option>
								</select>
							</div>
						</div>
					</div>
				</div>

				<!-- Right Column - Patient & Insurance Info -->
				<div class="space-y-6">
					<!-- Patient Information Card -->
					<div class="bg-white shadow rounded-lg p-6">
						<h2 class="text-lg font-medium text-gray-900 mb-4">Patient Information</h2>
						<p class="text-sm text-gray-600 mb-4">
							Select a patient for this invoice.
						</p>

						<div class="mb-4">
							<div class="relative">
								<input
									v-model="patientSearch"
									@focus="showPatientDropdown = true"
									type="text"
									placeholder="Search patients..."
									class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								/>
								<div
									class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
								>
									<svg
										class="h-5 w-5 text-gray-400"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
										/>
									</svg>
								</div>
							</div>

							<!-- Patient Dropdown -->
							<div
								v-if="showPatientDropdown"
								class="absolute z-10 mt-1 w-full bg-white border border-gray-300 rounded-md shadow-lg"
							>
								<div
									v-for="patient in filteredPatients"
									:key="patient.id"
									@click="selectPatient(patient)"
									class="px-4 py-2 hover:bg-gray-50 cursor-pointer border-b last:border-b-0"
								>
									<div class="font-medium">{{ patient.name }}</div>
									<div class="text-sm text-gray-500">{{ patient.id }}</div>
								</div>
							</div>
						</div>

						<!-- Selected Patient -->
						<div v-if="selectedPatient" class="border border-gray-200 rounded-lg p-4">
							<div class="flex items-center mb-3">
								<div
									class="h-10 w-10 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center text-white font-medium"
								>
									{{ selectedPatient.initials }}
								</div>
								<div class="ml-3">
									<div class="font-medium">{{ selectedPatient.name }}</div>
									<div class="text-sm text-gray-500">
										{{ selectedPatient.age }} • {{ selectedPatient.gender }} •
										ID: {{ selectedPatient.id }}
									</div>
								</div>
							</div>
							<div class="space-y-1 text-sm">
								<div><strong>Email:</strong> {{ selectedPatient.email }}</div>
								<div><strong>Phone:</strong> {{ selectedPatient.phone }}</div>
								<div><strong>Address:</strong> {{ selectedPatient.address }}</div>
							</div>
							<button
								class="mt-3 text-blue-600 hover:text-blue-800 text-sm font-medium"
							>
								View patient details
							</button>
						</div>
					</div>

					<!-- Insurance Information Card -->
					<div class="bg-white shadow rounded-lg p-6">
						<h2 class="text-lg font-medium text-gray-900 mb-4">
							Insurance Information
						</h2>
						<p class="text-sm text-gray-600 mb-4">Patient's insurance details.</p>

						<div class="flex items-center justify-between mb-4">
							<label class="text-sm font-medium text-gray-700"
								>Bill to Insurance</label
							>
							<button
								@click="billToInsurance = !billToInsurance"
								:class="billToInsurance ? 'bg-blue-600' : 'bg-gray-300'"
								class="relative inline-flex h-6 w-11 items-center rounded-full transition-colors"
							>
								<span
									:class="billToInsurance ? 'translate-x-6' : 'translate-x-1'"
									class="inline-block h-4 w-4 transform bg-white rounded-full transition-transform"
								></span>
							</button>
						</div>

						<div v-if="billToInsurance && selectedPatient" class="space-y-4">
							<div class="border border-gray-200 rounded-lg p-4">
								<div class="font-medium text-blue-600 mb-1">
									{{ selectedPatient.insurance.provider }}
								</div>
								<div class="text-sm space-y-1">
									<div>
										<strong>Policy #:</strong>
										{{ selectedPatient.insurance.policyNumber }}
									</div>
									<div>
										<strong>Group #:</strong>
										{{ selectedPatient.insurance.groupNumber }}
									</div>
									<div>
										<strong>Coverage:</strong>
										{{ selectedPatient.insurance.coverage }}
									</div>
								</div>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Copay Amount</label
								>
								<input
									v-model="copayAmount"
									type="number"
									step="0.01"
									placeholder="0.00"
									class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
								/>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Coverage Verification</label
								>
								<div class="space-y-2">
									<label class="flex items-center">
										<input
											v-model="coverageVerification"
											value="verified"
											type="radio"
											class="h-4 w-4 text-blue-600 border-gray-300"
										/>
										<span class="ml-2 text-sm">Verified</span>
									</label>
									<label class="flex items-center">
										<input
											v-model="coverageVerification"
											value="pending"
											type="radio"
											class="h-4 w-4 text-blue-600 border-gray-300"
										/>
										<span class="ml-2 text-sm">Pending Verification</span>
									</label>
									<label class="flex items-center">
										<input
											v-model="coverageVerification"
											value="not-covered"
											type="radio"
											class="h-4 w-4 text-blue-600 border-gray-300"
										/>
										<span class="ml-2 text-sm">Not Covered</span>
									</label>
								</div>
							</div>
						</div>
					</div>

					<!-- Payment Options Card -->
					<div class="bg-white shadow rounded-lg p-6">
						<h2 class="text-lg font-medium text-gray-900 mb-4">Payment Options</h2>

						<div class="mb-4">
							<label class="block text-sm font-medium text-gray-700 mb-3"
								>Accepted Payment Methods</label
							>
							<div class="grid grid-cols-2 gap-3">
								<label
									v-for="method in paymentMethods"
									:key="method.id"
									class="flex items-center"
								>
									<input
										v-model="method.enabled"
										type="checkbox"
										class="h-4 w-4 text-blue-600 border-gray-300 rounded"
									/>
									<span class="ml-2 text-sm">{{ method.name }}</span>
								</label>
							</div>
						</div>

						<div class="flex items-center justify-between">
							<label class="text-sm font-medium text-gray-700"
								>Offer Payment Plan</label
							>
							<button
								@click="offerPaymentPlan = !offerPaymentPlan"
								:class="offerPaymentPlan ? 'bg-blue-600' : 'bg-gray-300'"
								class="relative inline-flex h-6 w-11 items-center rounded-full transition-colors"
							>
								<span
									:class="offerPaymentPlan ? 'translate-x-6' : 'translate-x-1'"
									class="inline-block h-4 w-4 transform bg-white rounded-full transition-transform"
								></span>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Invoice data
const invoice = ref({
	number: 'INV-008',
	date: '2025-06-28',
	dueDate: '2025-07-28',
	type: 'Standard Invoice',
	reference: '',
	items: [
		{
			selected: false,
			description: '',
			additionalDescription: '',
			quantity: 1,
			unitPrice: 0,
		},
		{
			selected: false,
			description: 'Blood Test - Basic Panel - $80.00',
			additionalDescription: '',
			quantity: 1,
			unitPrice: 80,
		},
	],
	notes: '',
	paymentTerms: 'Net 30 Days',
})

// Patient search and selection
const patientSearch = ref('')
const showPatientDropdown = ref(false)
const selectedPatient = ref(null)

const patients = ref([
	{
		id: 'P2343',
		name: 'John Smith',
		initials: 'JS',
		age: 45,
		gender: 'Male',
		email: 'john.smith@example.com',
		phone: '+1 (555) 123-4567',
		address: '123 Main Street, Apt 4B, New York, NY 10001',
		insurance: {
			provider: 'Blue Cross Blue Shield',
			policyNumber: 'BCBS12345789',
			groupNumber: 'GRP987654321',
			coverage: 'PPO',
		},
	},
	{
		id: 'P7024',
		name: 'David Miller',
		initials: 'DM',
		age: 52,
		gender: 'Male',
		email: 'david.miller@example.com',
		phone: '+1 (555) 987-6543',
		address: '456 Oak Avenue, Boston, MA 02101',
		insurance: {
			provider: 'Aetna',
			policyNumber: 'AET98765432',
			groupNumber: 'GRP123456789',
			coverage: 'HMO',
		},
	},
])

// Insurance and payment options
const billToInsurance = ref(true)
const copayAmount = ref('0.00')
const coverageVerification = ref('verified')
const offerPaymentPlan = ref(false)

const paymentMethods = ref([
	{ id: 'credit-card', name: 'Credit Card', enabled: true },
	{ id: 'debit-card', name: 'Debit Card', enabled: true },
	{ id: 'cash', name: 'Cash', enabled: true },
	{ id: 'check', name: 'Check', enabled: false },
	{ id: 'bank-transfer', name: 'Bank Transfer', enabled: true },
	{ id: 'insurance', name: 'Insurance', enabled: true },
	{ id: 'patient-portal', name: 'Patient Portal', enabled: true },
	{ id: 'payment-plan', name: 'Payment Plan', enabled: false },
])

// Computed properties for invoice calculations
const subtotal = computed(() => {
	return invoice.value.items.reduce((sum, item) => {
		return sum + item.quantity * item.unitPrice
	}, 0)
})

const tax = computed(() => {
	return subtotal.value * 0.08
})

const discount = computed(() => {
	return 0 // Can be made dynamic
})

const total = computed(() => {
	return subtotal.value + tax.value - discount.value
})

const filteredPatients = computed(() => {
	if (!patientSearch.value) return patients.value
	return patients.value.filter(
		(patient) =>
			patient.name.toLowerCase().includes(patientSearch.value.toLowerCase()) ||
			patient.id.toLowerCase().includes(patientSearch.value.toLowerCase()),
	)
})

// Methods
const addItem = () => {
	invoice.value.items.push({
		selected: false,
		description: '',
		additionalDescription: '',
		quantity: 1,
		unitPrice: 0,
	})
}

const removeItem = (index) => {
	invoice.value.items.splice(index, 1)
}

const selectPatient = (patient) => {
	selectedPatient.value = patient
	patientSearch.value = patient.name
	showPatientDropdown.value = false
}

const saveAsDraft = () => {
	console.log('Saving as draft...', {
		invoice: invoice.value,
		patient: selectedPatient.value,
		insurance: {
			billToInsurance: billToInsurance.value,
			copayAmount: copayAmount.value,
			coverageVerification: coverageVerification.value,
		},
		paymentOptions: {
			methods: paymentMethods.value.filter((m) => m.enabled),
			offerPaymentPlan: offerPaymentPlan.value,
		},
	})
}

const createInvoice = () => {
	console.log('Creating invoice...', {
		invoice: invoice.value,
		patient: selectedPatient.value,
		totals: {
			subtotal: subtotal.value,
			tax: tax.value,
			discount: discount.value,
			total: total.value,
		},
	})
}

// Initialize with first patient selected
onMounted(() => {
	selectedPatient.value = patients.value[0]
	patientSearch.value = patients.value[0].name
})

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
	if (!event.target.closest('.relative')) {
		showPatientDropdown.value = false
	}
}

onMounted(() => {
	document.addEventListener('click', handleClickOutside)
})
</script>
