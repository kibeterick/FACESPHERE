"""
Payment Processing System
Accept payments, invoicing, transaction history, and financial reports
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import uuid


class PaymentSystem:
    """Complete payment processing and financial management system"""
    
    def __init__(self, data_file='payments_data.json'):
        self.data_file = data_file
        self.transactions = []
        self.invoices = []
        self.customers = {}
        self.payment_methods = []
        self._load_data()
        
        # Payment gateway configuration (placeholder)
        self.gateways = {
            'stripe': {
                'api_key': os.getenv('STRIPE_API_KEY', '[stripe_key]'),
                'enabled': True
            },
            'paypal': {
                'client_id': os.getenv('PAYPAL_CLIENT_ID', '[paypal_id]'),
                'enabled': True
            },
            'square': {
                'access_token': os.getenv('SQUARE_ACCESS_TOKEN', '[square_token]'),
                'enabled': False
            }
        }
    
    def _load_data(self):
        """Load payment data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.transactions = data.get('transactions', [])
                    self.invoices = data.get('invoices', [])
                    self.customers = data.get('customers', {})
            except:
                pass
    
    def _save_data(self):
        """Save payment data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump({
                    'transactions': self.transactions,
                    'invoices': self.invoices,
                    'customers': self.customers
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving payment data: {e}")
    
    def process_payment(self, customer_id: str, amount: float, 
                       currency: str = 'USD', payment_method: str = 'card',
                       description: str = '', metadata: Dict = None) -> Dict:
        """Process a payment"""
        transaction_id = str(uuid.uuid4())[:12].upper()
        
        transaction = {
            'transaction_id': transaction_id,
            'customer_id': customer_id,
            'amount': amount,
            'currency': currency,
            'payment_method': payment_method,
            'description': description,
            'metadata': metadata or {},
            'status': 'completed',
            'created_at': datetime.now().isoformat(),
            'gateway': 'stripe',  # Default gateway
            'fee': round(amount * 0.029 + 0.30, 2),  # 2.9% + $0.30
            'net_amount': round(amount - (amount * 0.029 + 0.30), 2)
        }
        
        self.transactions.append(transaction)
        self._save_data()
        
        print(f"💳 Payment processed: ${amount} {currency}")
        print(f"   Transaction ID: {transaction_id}")
        print(f"   Status: {transaction['status']}")
        
        return transaction
    
    def create_invoice(self, customer_id: str, items: List[Dict],
                      due_date: str = None, notes: str = '') -> Dict:
        """Create an invoice"""
        invoice_id = f"INV-{str(uuid.uuid4())[:8].upper()}"
        
        # Calculate totals
        subtotal = sum(item['quantity'] * item['price'] for item in items)
        tax_rate = 0.10  # 10% tax
        tax = round(subtotal * tax_rate, 2)
        total = round(subtotal + tax, 2)
        
        invoice = {
            'invoice_id': invoice_id,
            'customer_id': customer_id,
            'items': items,
            'subtotal': subtotal,
            'tax': tax,
            'tax_rate': tax_rate,
            'total': total,
            'currency': 'USD',
            'status': 'pending',
            'due_date': due_date,
            'notes': notes,
            'created_at': datetime.now().isoformat(),
            'paid_at': None,
            'payment_link': f'https://akira-pay.com/invoice/{invoice_id}'
        }
        
        self.invoices.append(invoice)
        self._save_data()
        
        print(f"📄 Invoice created: {invoice_id}")
        print(f"   Total: ${total}")
        print(f"   Status: {invoice['status']}")
        
        return invoice
    
    def pay_invoice(self, invoice_id: str, payment_method: str = 'card') -> Dict:
        """Pay an invoice"""
        invoice = None
        for inv in self.invoices:
            if inv['invoice_id'] == invoice_id:
                invoice = inv
                break
        
        if not invoice:
            return {
                'success': False,
                'message': 'Invoice not found'
            }
        
        if invoice['status'] == 'paid':
            return {
                'success': False,
                'message': 'Invoice already paid'
            }
        
        # Process payment
        transaction = self.process_payment(
            customer_id=invoice['customer_id'],
            amount=invoice['total'],
            currency=invoice['currency'],
            payment_method=payment_method,
            description=f"Payment for invoice {invoice_id}"
        )
        
        # Update invoice
        invoice['status'] = 'paid'
        invoice['paid_at'] = datetime.now().isoformat()
        invoice['transaction_id'] = transaction['transaction_id']
        
        self._save_data()
        
        print(f"✅ Invoice {invoice_id} paid successfully")
        
        return {
            'success': True,
            'invoice': invoice,
            'transaction': transaction
        }
    
    def refund_payment(self, transaction_id: str, amount: float = None,
                      reason: str = '') -> Dict:
        """Refund a payment"""
        transaction = None
        for txn in self.transactions:
            if txn['transaction_id'] == transaction_id:
                transaction = txn
                break
        
        if not transaction:
            return {
                'success': False,
                'message': 'Transaction not found'
            }
        
        refund_amount = amount or transaction['amount']
        
        refund = {
            'refund_id': str(uuid.uuid4())[:12].upper(),
            'transaction_id': transaction_id,
            'amount': refund_amount,
            'currency': transaction['currency'],
            'reason': reason,
            'status': 'completed',
            'created_at': datetime.now().isoformat()
        }
        
        # Update transaction status
        transaction['status'] = 'refunded'
        transaction['refund'] = refund
        
        self._save_data()
        
        print(f"💰 Refund processed: ${refund_amount}")
        print(f"   Refund ID: {refund['refund_id']}")
        
        return refund
    
    def add_customer(self, customer_id: str, name: str, email: str,
                    phone: str = '', address: Dict = None) -> Dict:
        """Add a customer"""
        customer = {
            'customer_id': customer_id,
            'name': name,
            'email': email,
            'phone': phone,
            'address': address or {},
            'created_at': datetime.now().isoformat(),
            'total_spent': 0,
            'transaction_count': 0,
            'status': 'active'
        }
        
        self.customers[customer_id] = customer
        self._save_data()
        
        print(f"👤 Customer added: {name}")
        
        return customer
    
    def get_customer(self, customer_id: str) -> Optional[Dict]:
        """Get customer details"""
        return self.customers.get(customer_id)
    
    def update_customer_stats(self, customer_id: str, amount: float):
        """Update customer statistics"""
        if customer_id in self.customers:
            self.customers[customer_id]['total_spent'] += amount
            self.customers[customer_id]['transaction_count'] += 1
            self._save_data()
    
    def get_transactions(self, customer_id: str = None, 
                        status: str = None, limit: int = 50) -> List[Dict]:
        """Get transaction history"""
        transactions = self.transactions
        
        if customer_id:
            transactions = [t for t in transactions if t['customer_id'] == customer_id]
        
        if status:
            transactions = [t for t in transactions if t['status'] == status]
        
        return transactions[-limit:]
    
    def get_invoices(self, customer_id: str = None, 
                    status: str = None) -> List[Dict]:
        """Get invoices"""
        invoices = self.invoices
        
        if customer_id:
            invoices = [i for i in invoices if i['customer_id'] == customer_id]
        
        if status:
            invoices = [i for i in invoices if i['status'] == status]
        
        return invoices
    
    def get_financial_report(self, period: str = 'month') -> Dict:
        """Generate financial report"""
        now = datetime.now()
        
        # Filter transactions by period
        if period == 'today':
            transactions = [
                t for t in self.transactions 
                if datetime.fromisoformat(t['created_at']).date() == now.date()
            ]
        elif period == 'week':
            week_ago = now.timestamp() - (7 * 24 * 60 * 60)
            transactions = [
                t for t in self.transactions 
                if datetime.fromisoformat(t['created_at']).timestamp() > week_ago
            ]
        elif period == 'month':
            transactions = [
                t for t in self.transactions 
                if datetime.fromisoformat(t['created_at']).month == now.month
            ]
        else:
            transactions = self.transactions
        
        # Calculate metrics
        total_revenue = sum(t['amount'] for t in transactions if t['status'] == 'completed')
        total_fees = sum(t.get('fee', 0) for t in transactions if t['status'] == 'completed')
        net_revenue = sum(t.get('net_amount', 0) for t in transactions if t['status'] == 'completed')
        total_refunds = sum(t['amount'] for t in transactions if t['status'] == 'refunded')
        
        transaction_count = len(transactions)
        avg_transaction = total_revenue / transaction_count if transaction_count > 0 else 0
        
        # Payment method breakdown
        payment_methods = {}
        for t in transactions:
            method = t['payment_method']
            payment_methods[method] = payment_methods.get(method, 0) + t['amount']
        
        return {
            'period': period,
            'total_revenue': round(total_revenue, 2),
            'total_fees': round(total_fees, 2),
            'net_revenue': round(net_revenue, 2),
            'total_refunds': round(total_refunds, 2),
            'transaction_count': transaction_count,
            'average_transaction': round(avg_transaction, 2),
            'payment_methods': payment_methods,
            'generated_at': datetime.now().isoformat()
        }
    
    def get_statistics(self) -> Dict:
        """Get payment statistics"""
        total_transactions = len(self.transactions)
        completed_transactions = len([t for t in self.transactions if t['status'] == 'completed'])
        refunded_transactions = len([t for t in self.transactions if t['status'] == 'refunded'])
        
        total_revenue = sum(t['amount'] for t in self.transactions if t['status'] == 'completed')
        total_invoices = len(self.invoices)
        pending_invoices = len([i for i in self.invoices if i['status'] == 'pending'])
        paid_invoices = len([i for i in self.invoices if i['status'] == 'paid'])
        
        return {
            'total_transactions': total_transactions,
            'completed_transactions': completed_transactions,
            'refunded_transactions': refunded_transactions,
            'total_revenue': round(total_revenue, 2),
            'total_invoices': total_invoices,
            'pending_invoices': pending_invoices,
            'paid_invoices': paid_invoices,
            'total_customers': len(self.customers)
        }
    
    def create_subscription(self, customer_id: str, plan_name: str,
                          amount: float, interval: str = 'monthly') -> Dict:
        """Create a subscription"""
        subscription_id = f"SUB-{str(uuid.uuid4())[:8].upper()}"
        
        subscription = {
            'subscription_id': subscription_id,
            'customer_id': customer_id,
            'plan_name': plan_name,
            'amount': amount,
            'interval': interval,
            'status': 'active',
            'created_at': datetime.now().isoformat(),
            'next_billing_date': self._calculate_next_billing(interval),
            'cancel_at_period_end': False
        }
        
        print(f"🔄 Subscription created: {plan_name}")
        print(f"   Amount: ${amount}/{interval}")
        
        return subscription
    
    def _calculate_next_billing(self, interval: str) -> str:
        """Calculate next billing date"""
        from datetime import timedelta
        now = datetime.now()
        
        if interval == 'monthly':
            next_date = now + timedelta(days=30)
        elif interval == 'yearly':
            next_date = now + timedelta(days=365)
        elif interval == 'weekly':
            next_date = now + timedelta(days=7)
        else:
            next_date = now + timedelta(days=30)
        
        return next_date.isoformat()


# Global instance
payment_system = PaymentSystem()


if __name__ == '__main__':
    print("="*60)
    print("💳 Payment Processing System - Test")
    print("="*60)
    
    # Add customer
    customer = payment_system.add_customer(
        customer_id='cust123',
        name='John Doe',
        email='[email]',
        phone='+1234567890'
    )
    print(f"\n✅ Customer added: {customer['name']}")
    
    # Process payment
    transaction = payment_system.process_payment(
        customer_id='cust123',
        amount=99.99,
        currency='USD',
        payment_method='card',
        description='Product purchase'
    )
    print(f"✅ Payment processed: ${transaction['amount']}")
    
    # Create invoice
    invoice = payment_system.create_invoice(
        customer_id='cust123',
        items=[
            {'name': 'Product A', 'quantity': 2, 'price': 50.00},
            {'name': 'Product B', 'quantity': 1, 'price': 75.00}
        ],
        due_date='2026-03-01'
    )
    print(f"✅ Invoice created: {invoice['invoice_id']}")
    
    # Get statistics
    stats = payment_system.get_statistics()
    print(f"\n📊 Statistics:")
    print(f"   Total transactions: {stats['total_transactions']}")
    print(f"   Total revenue: ${stats['total_revenue']}")
    print(f"   Total invoices: {stats['total_invoices']}")
    
    # Generate report
    report = payment_system.get_financial_report('month')
    print(f"\n📈 Financial Report:")
    print(f"   Revenue: ${report['total_revenue']}")
    print(f"   Net: ${report['net_revenue']}")
    print(f"   Transactions: {report['transaction_count']}")
    
    print("\n✅ Payment system tested!")
